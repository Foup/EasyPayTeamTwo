import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, \
    ElementNotInteractableException, ElementNotVisibleException
from src.Utilities.logger import logger


class Page(object):

    log = logger()

    def __init__(self, driver=None, base_url=''):
        self.driver = driver
        if base_url:
            self.driver.get(base_url)

    def get_page_title(self):
        return self.driver.title

    def get_locator_type(self, locator_type):
        locator_type = locator_type.lower()
        locator_types = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'class': By.CLASS_NAME,
            'link': By.LINK_TEXT
        }
        if locator_type in locator_types:
            return locator_types[locator_type]
        self.log.info("Locator type: %s not supported!" % locator_type)
        raise NoSuchElementException

    def get_element(self, locator, locator_type='xpath'):
        try:
            element = self.driver.find_element(
                self.get_locator_type(locator_type), locator)
            self.log.info("Element with locator: %s By type: "
                          "%s  Found!" % (locator, locator_type))
            return element
        except NoSuchElementException:
            self.log.error("Element with locator: %s By type:"
                           " %s  Not Found!" % (locator, locator_type))
            get_screenshot(self.driver, "Element not found")
            raise NoSuchElementException

    def click_on_element(self, locator, locator_type='xpath'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Click on element with locator: %s and"
                          " locator type: %s" % (locator, locator_type))
        except ElementNotInteractableException:
            self.log.warning("Can not click on element with locator: %s and"
                             " locator type: %s" % (locator, locator_type))
            get_screenshot(self.driver, "Element not interactable")
            raise ElementNotInteractableException
        return self

    def send_keys_to_element(self, data, locator, locator_type="xpath"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info(" Data %s successfully send to element with locator:"
                          " %s and locator type: %s"
                          % (data, locator, locator_type))
        except ElementNotInteractableException:
            self.log.warning(" Failed to send: %s to the element with locator:"
                             " %s and locator type: %s" %
                             (data, locator, locator_type))
            get_screenshot(self.driver, "Element not interactable")
            raise ElementNotInteractableException
        return self

    def is_element_present(self, locator, locator_type='xpath'):
        try:
            element = self.get_element(locator, locator_type)
            if element is None:
                self.log.error("Element with locator %s and locator type: "
                               "%s NOT FOUND!" % (locator, locator_type))
                get_screenshot(self.driver, "Element is None")
                return False
            self.log.info("Element with locator %s and locator type: "
                          "%s Found!" % (locator, locator_type))
            return True
        except NoSuchElementException:
            return False

    def is_button_enabled(self, locator, locator_type='xpath'):
        try:
            element = self.get_element(locator, locator_type)
            if element is None:
                self.log.error("Element with locator %s and locator type: "
                               "%s NOT FOUND!" % (locator, locator_type))
                get_screenshot(self.driver, "Element is None")
                return False
            self.log.info("Element with locator %s and locator type: "
                          "%s Found!" % (locator, locator_type))
            return element.is_enabled() and element.is_displayed()
        except NoSuchElementException:
            self.log.error("Element with locator %s and locator type: "
                           "%s Not Found!" % (locator, locator_type))
            get_screenshot(self.driver, "Button not found")
            return False

    def wait_for_element(self, locator, locator_type='xpath', timeout=20):
        try:
            self.log.info("Waiting for maximum: %d for element"
                          " to be visible on the page" % timeout)
            WebDriverWait(self.driver, timeout)\
                .until(expected_conditions.visibility_of_element_located(
                    (self.get_locator_type(locator_type), locator)))
            self.log.info("Element with locator: %s appeared on the page"
                          % locator)
        except NoSuchElementException:
            self.log.error("Element with locator %s and locator type: "
                           "%s NOT FOUND!" % (locator, locator_type))
            get_screenshot(self.driver, "Element not found")
            raise NoSuchElementException
        except ElementNotVisibleException:
            self.log.error("Element with locator: %s is not"
                           " visible on the page" % locator)
            get_screenshot(self.driver, "Element not visible")
            raise ElementNotVisibleException
        return self

    def is_element_visible(self, locator, locator_type='xpath'):
        try:
            element = self.get_element(locator, locator_type)
            if element is None:
                self.log.error("Element with locator %s and locator type: "
                               "%s NOT FOUND!" % (locator, locator_type))
                get_screenshot(self.driver, "Element is None")
                return False
            self.log.info("Element with locator %s and locator type: "
                          "%s Found!" % (locator, locator_type))

            return element.is_displayed()
        except NoSuchElementException:
            return False

    def is_displayed(self, locator, locator_type='xpath'):
        return self.is_element_visible(locator, locator_type)

    def wait_for_element_disappear(self, locator,
                                   locator_type='xpath', timeout=20):
        try:
            self.log.info("Waiting for maximum: %d for element"
                          " to disappear from the page" % timeout)
            WebDriverWait(self.driver, timeout)\
                .until(expected_conditions.invisibility_of_element_located(
                    (self.get_locator_type(locator_type), locator)))
            self.log.info("Element with locator: %s disappeared from the page"
                          % locator)
        except NoSuchElementException:
            self.log.error("Element with locator %s and locator type: "
                           "%s NOT FOUND!" % (locator, locator_type))
            get_screenshot(self.driver, "Element not found")
            raise NoSuchElementException
        except AttributeError:
            self.log.error("Element with locator: %s is"
                           " visible on the page: %s" % locator, self.get_page_title())
            get_screenshot(self.driver, "Element visible")
            raise AttributeError
        return self


def get_screenshot(driver, scr_name):
    allure.attach(driver.get_screenshot_as_png(),
                  name=scr_name,
                  attachment_type=AttachmentType.PNG,
                  extension=AttachmentType.PNG.extension)

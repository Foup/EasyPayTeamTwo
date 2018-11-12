from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    def __init__(self, driver=None):
        self.driver = driver

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        locatorTypes = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'class': By.CLASS_NAME,
            'link': By.LINK_TEXT
        }
        if locatorType in locatorTypes:
            return locatorTypes[locatorType]
        else:
            print("Locator type: " + locatorType + " not supported!")
            return None

    def getElement(self, locator, locatorType='xpath'):
        try:
            element = self.driver.find_element(self.getLocatorType(locatorType), locator)
            print("Element with locator: " + locator + " By type: " + locatorType + " Found!")
            return element
        except:
            print("Element with locator: " + locator + " By type: " + locatorType + " Not Found!")
            return None


    def clickOnElement(self, locator, locatorType='xpath'):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Click on element with locator: " + locator + " and locator type: " + locatorType)
        except:
            print("Can not click on element with locator: " + locator + "and locator type: " + locatorType)
        return self

    def sendKeysToElement(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print(" Data " + data + "successfully send to element with locator: " + locator + "and locator type: " + locatorType)
        except:
            print(" Failed to send: " + data + " to the element with locator: " + locator + "and locator type: " + locatorType)
        return self

    def isElementPresent(self, locator, locatorType='xpath'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element with locator " + locator + " and locator type: " + locatorType)
                return True
            else:
                print("Element with locator " + locator + " and locator type: " + locatorType + " NOT FOUND!")
                return False
        except:
            print("Element with locator " + locator + " and locator type: " + locatorType + " NOT FOUND!")
            return False

    def is_button_enabled(self, locator, locatorType='xpath'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element with locator " + locator + " and locator type: " + locatorType)
                return element.is_enabled()
            else:
                print("Element with locator " + locator + " and locator type: " + locatorType + " NOT FOUND!")
                return False
        except:
            print("Element with locator " + locator + " and locator type: " + locatorType + " NOT FOUND!")
            return False

    def waitForElement(self, locator, locatorType='xpath', timeout=10):
        try:
            print("Waiting for maximum: " + str(timeout) + "for element to be visible on the page")
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located((self.getLocatorType(locatorType),locator)))
            print("Element with locator: " + locator + ' appeared on the page')
        except:
            print("Element with locator: " + locator + ' not visible on the page')
        return self

    def is_displayed(self, element):
        return self.isElementPresent(element)

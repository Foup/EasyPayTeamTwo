import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.locators import PathToCounters, SelectedAddress
from src.PageObjects.login_page import Login

''' Verify that it is a warning message when new value is less than previous.'''

class TestCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_counter_value(self):
        driver = self.driver
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.address_li).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="countersTable"]/tbody/tr')))
        assert driver.find_element(By.XPATH, SelectedAddress.utility).is_displayed()
        oldValue = int(driver.find_element_by_class_name('oldValue').text)
        newValue = oldValue - 5
        driver.find_element_by_class_name('change-value').click()
        WebDriverWait(driver, 7).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'modal-dialog')))
        WebDriverWait(driver, 7).until(
            expected_conditions.visibility_of_element_located((By.ID, 'newCurrentValue')))
        driver.find_element_by_id('newCurrentValue').send_keys(newValue)
        driver.find_element_by_class_name('js-apply').click()
        try:
            driver.find_element_by_id('confirm-dialog')
        except NoSuchElementException:
            print('Confirm dialog missing')
            raise NoSuchElementException
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

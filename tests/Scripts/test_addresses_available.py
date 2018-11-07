from selenium import webdriver
from tests.PageObject import login_page
from tests.PageObject.Locators import Locator
from selenium.webdriver.common.by import By


class TestAddressesAvailable:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login_page.login_inspector(driver)

    def test_addresses_available(self):
        driver = self.driver
        driver.find_element(By.XPATH, Locator.counters_menu_item).click()
        driver.find_element(By.XPATH, Locator.counters_dropdown).click()
        assert driver.find_element(By.XPATH, Locator.counters_addresses_list).is_displayed()

    def teardown(self):
        self.driver.quit()

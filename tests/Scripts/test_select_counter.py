from selenium import webdriver
from tests.PageObject import login_page
from tests.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
import time


class TestSelectCounter:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login_page.login_inspector(driver)

    def test_select_counter(self):
        driver = self.driver
        driver.find_element(By.XPATH, Locator.counters_menu_item).click()
        driver.find_element(By.XPATH, Locator.counters_dropdown).click()
        driver.find_element(By.XPATH, Locator.counters_address_li).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, Locator.counters_utility).is_displayed()
        assert driver.find_element(By.XPATH, Locator.counters_old_value).is_displayed()
        assert driver.find_element(By.XPATH, Locator.counters_current_value).is_displayed()
        assert driver.find_element(By.XPATH, Locator.counters_activate_button).is_displayed()
        assert driver.find_element(By.XPATH, Locator.counters_fixed_button).is_displayed()
        assert driver.find_element(By.XPATH, Locator.counters_init_values_button).is_displayed()
        assert driver.find_element(By.XPATH, Locator.counters_new_value_button).is_displayed()

    def teardown(self):
        self.driver.quit()

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.PageObjects.Login_Page import Login
from src.Locators import PathToCounters
from src.Locators import SelectedAddress
from selenium.webdriver.common.by import By
import time


class TestSelectCounter:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_select_counter(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.counters_menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 7).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="countersTable"]/tbody/tr')))
        assert driver.find_element(By.XPATH, SelectedAddress.counters_utility).is_displayed()
        assert driver.find_element(By.XPATH, SelectedAddress.counters_old_value).is_displayed()
        assert driver.find_element(By.XPATH, SelectedAddress.counters_current_value).is_displayed()
        assert driver.find_element(By.XPATH, SelectedAddress.counters_activate_button).is_displayed()
        assert driver.find_element(By.XPATH, SelectedAddress.counters_fixed_button).is_displayed()
        assert driver.find_element(By.XPATH, SelectedAddress.counters_init_values_button).is_displayed()
        assert driver.find_element(By.XPATH, SelectedAddress.counters_new_value_button).is_displayed()

    def teardown(self):
        self.driver.quit()

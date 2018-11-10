from selenium import webdriver
from src.PageObjects.login_page import Login
from src.locators import PathToCounters
from src.locators import SelectedAddress
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestValidCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()


    def test_fix_value(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.counters_menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.counters_fixed_button)))
        prev_status=driver.find_element((By.XPATH, SelectedAddress.counters_fixed_button_label))
        driver.find_element(By.XPATH, SelectedAddress.counters_fixed_button).click()
        new_status=driver.find_element((By.XPATH, SelectedAddress.counters_fixed_button_label))
        assert prev_status==new_status

    def teardown(self):
        self.driver.quit()

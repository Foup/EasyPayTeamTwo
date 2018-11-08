from selenium import webdriver
from src.PageObjects.Login_Page import Login
from src.Locators import PathToCounters
from src.Locators import SelectedAddress
from src.Locators import NewValue
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestNewCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_new_counter_value(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.counters_menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.counters_new_value_button)))
        old_value=int(driver.find_element(By.XPATH, SelectedAddress.counters_current_value).get_attribute('data-value'))
        driver.find_element(By.XPATH, SelectedAddress.counters_new_value_button).click()
        driver.find_element(By.XPATH, NewValue.new_value_field).click()
        driver.find_element(By.XPATH, NewValue.new_value_field).send_keys(old_value+1)
        driver.find_element(By.XPATH, NewValue.new_value_apply_button).click()
        time.sleep(10)
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, Locator.new_counter_value)))
        assert int(driver.find_element(By.XPATH, SelectedAddress.counters_current_value).get_attribute('data-value'))==old_value+1


    def teardown(self):
        self.driver.quit()

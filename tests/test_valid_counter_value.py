from selenium import webdriver
from src.PageObjects.Login_Page import Login
from src.Locators import PathToCounters
from src.Locators import SelectedAddress
from src.Locators import NewValue
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

    def test_valid_counter_value(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.counters_menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.counters_new_value_button)))
        driver.find_element(By.XPATH, SelectedAddress.counters_new_value_button).click()
        driver.find_element(By.XPATH, NewValue.new_value_field).click()
        driver.find_element(By.XPATH, NewValue.new_value_field).send_keys(-2)
        driver.find_element(By.XPATH, NewValue.new_value_apply_button).click()
        assert driver.find_element(By.XPATH, NewValue.new_value_wrong_value_message).is_displayed()
        driver.find_element(By.XPATH, NewValue.new_value_field).clear()
        driver.find_element(By.XPATH, NewValue.new_value_field).send_keys(27)
        driver.find_element(By.XPATH, NewValue.new_value_apply_button).click()
        time.sleep(8)
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.counters_current_value)))
        assert int(driver.find_element(By.XPATH, SelectedAddress.counters_current_value).get_attribute('data-value'
                                                                                          )) == 27
        driver.find_element(By.XPATH, SelectedAddress.counters_new_value_button).click()
        driver.find_element(By.XPATH, NewValue.new_value_field).click()
        driver.find_element(By.XPATH, NewValue.new_value_field).send_keys(123456789)
        driver.find_element(By.XPATH, NewValue.new_value_apply_button).click()
        assert driver.find_element(By.XPATH, NewValue.new_value_wrong_value_message).is_displayed()

    def teardown(self):
        self.driver.quit()

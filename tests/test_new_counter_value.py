from selenium import webdriver
from src.PageObjects.login_page import Login
from src.locators import PathToCounters
from src.locators import SelectedAddress
from src.locators import NewValue
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
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.address_li).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.new_value_button)))
        old_value=int(driver.find_element(By.XPATH, SelectedAddress.current_value).get_attribute('data-value'))
        driver.find_element(By.XPATH, SelectedAddress.new_value_button).click()
        driver.find_element(By.XPATH, NewValue.field).click()
        driver.find_element(By.XPATH, NewValue.field).send_keys(old_value + 1)
        driver.find_element(By.XPATH, NewValue.apply_button).click()
        time.sleep(10)
        driver.find_element(By.XPATH, PathToCounters.dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.address_li).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.current_value)))
        assert int(driver.find_element(By.XPATH, SelectedAddress.current_value).get_attribute('data-value')) == old_value + 1


    def teardown(self):
        self.driver.quit()

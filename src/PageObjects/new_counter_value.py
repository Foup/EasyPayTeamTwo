from selenium import webdriver
from src.PageObjects.Login_Page import Login
from src.locators import PathToCounters
from src.locators import SelectedAddress
from src.locators import NewValue
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class CounterValue:

    def ClickNewValueButton(driver):
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.counters_new_value_button)))
        driver.find_element(By.XPATH, SelectedAddress.counters_new_value_button).click()
        return driver

    def SetNewValue(driver,value):
        driver.find_element(By.XPATH, NewValue.new_value_field).clear()
        driver.find_element(By.XPATH, NewValue.new_value_field).click()
        driver.find_element(By.XPATH, NewValue.new_value_field).send_keys(value)
        driver.find_element(By.XPATH, NewValue.new_value_apply_button).click()
        return driver

    def WrongMessagePresent(driver):
        return driver.find_element(By.XPATH, NewValue.new_value_wrong_value_message)\
            .is_displayed()

    def GetCurrentValue(driver):
        return int(driver.find_element(By.XPATH, SelectedAddress.counters_current_value)\
                   .get_attribute('data-value'))

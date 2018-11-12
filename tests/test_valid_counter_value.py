from selenium import webdriver
from src.PageObjects.login_page import Login
import time
from src.PageObjects.get_address import GetAddress
from src.PageObjects.new_counter_value import CounterValue
from src.PageObjects.Counter_Page import OpenCounterPage


class TestValidCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_valid_counter_value(self):
        driver = self.driver
        time.sleep(7)
        OpenCounterPage.CounterPage(driver)
        GetAddress.ChooseAddress(driver)
        CounterValue.ClickNewValueButton(driver)
        CounterValue.SetNewValue(driver,-1)
        assert CounterValue.WrongMessagePresent(driver)
        value=CounterValue.GetCurrentValue(driver)
        CounterValue.SetNewValue(driver,value+1)
        time.sleep(7)
        GetAddress.ChooseAddress(driver)
        time.sleep(5)
        assert CounterValue.GetCurrentValue(driver)==value+1
        CounterValue.ClickNewValueButton(driver)
        CounterValue.SetNewValue(driver, 123456789)
        assert CounterValue.WrongMessagePresent(driver)

    def teardown(self):
        self.driver.quit()

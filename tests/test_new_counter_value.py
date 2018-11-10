from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from src.PageObjects.Login_Page import Login
import time
from src.PageObjects.get_address import GetAddress
from src.PageObjects.Counter_Page import OpenCounterPage
from src.PageObjects.new_counter_value import NewValue


class TestNewCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_new_counter_value(self):
        driver: WebDriver = self.driver
        time.sleep(7)
        OpenCounterPage.CounterPage(driver)
        GetAddress.ChooseAddress(driver)
        NewValue.ClickNewValueButton(driver)
        value = NewValue.GetCurrentValue(driver)
        NewValue.SetNewValue(driver, value + 1)
        time.sleep(7)
        GetAddress.ChooseAddress(driver)
        time.sleep(5)
        assert NewValue.GetCurrentValue(driver) == value + 1

    def teardown(self):
        self.driver.quit()
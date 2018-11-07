import time

from selenium import webdriver
from src.Login_Page import Login


class TestAddressesAvailable:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_addresses_available(self):
        time.sleep(2)

    def teardown(self):
        self.driver.quit()



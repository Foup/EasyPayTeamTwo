import time
from selenium import webdriver
from src.PageObjects.login_page import Login
from src.PageObjects.counters_page import Counters


class TestAddressesAvailable:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_addresses_available(self):
        driver = self.driver
        counters = Counters(driver)
        counters.wait_for_login()\
            .open_counters_page()\
            .expand_counters_dropdown()\
            .wait_for_panel()
        assert counters.find_addresses_list().is_displayed()
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

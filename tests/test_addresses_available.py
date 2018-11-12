import time
from selenium import webdriver
from src.PageObjects.login_page import Login
from src.PageObjects.counters_page import Counters
from src.locators import HomePage, PathToCounters


''' Verify that the list of clients addresses assigned
 to the inspector is available.'''


class TestAddressesAvailable:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_addresses_available(self):
        driver = self.driver
        counters = Counters(driver)
        counters.waitForElement(HomePage.display_name, 'xpath')\
            .open_counters_page()\
            .expand_counters_dropdown()\
            .waitForElement(PathToCounters.panel, 'xpath')
        assert counters.isElementPresent(PathToCounters.addresses_list, 'xpath')
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.PageObjects.counters_page import Counters
from src.locators import PathToCounters, SelectedAddress, NewValue

from src.PageObjects.login_page import Login
from src.PageObjects.nav_menu import NavMenu


''' Verify that it is a warning message when new value is less than previous.'''

class TestCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_counter_value(self):
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address()
        oldValue = counters.get_old_value()
        newValue = oldValue - 5
        counters.open_new_value_modal()\
            .set_new_value(newValue)
        assert counters.is_displayed(NewValue.confirm_dialog)
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

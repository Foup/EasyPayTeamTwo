import time

from selenium import webdriver

from src.PageObjects.counters_page import Counters
from src.locators import NewValue

from src.PageObjects.login_page import Login


''' Verify that it is a warning message
when new value is less than previous.'''


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
        old_value = counters.get_old_value()
        new_value = old_value - 5
        counters.open_new_value_modal()\
            .set_new_value(new_value)
        assert counters.is_displayed(NewValue.confirm_dialog)
        time.sleep(2)

    def teardown(self):
        self.driver.quit()

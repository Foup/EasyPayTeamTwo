from selenium import webdriver
from src.PageObjects.login_page import Login
import time
from src.PageObjects.counters_page import Counters


class TestNewCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_new_counter_value(self):
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address()
        value = counters.get_current_value()
        counters.open_new_value_modal() \
            .set_new_value(value+1)
        time.sleep(10)
        counters.choose_address()
        time.sleep(5)
        assert counters.get_current_value() == value + 1

    def teardown(self):
        self.driver.quit()

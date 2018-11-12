from selenium import webdriver
from src.PageObjects.login_page import Login
from src.locators import SelectedAddress

from src.PageObjects.counters_page import Counters


'''Verify that the counter can be initialized with values if it has none.'''


class TestSelectCounter:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_select_counter(self):
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address()
        assert counters.is_displayed(SelectedAddress.utility)
        assert counters.is_displayed(SelectedAddress.old_value)
        assert counters.is_displayed(SelectedAddress.current_value)
        assert counters.is_displayed(SelectedAddress.activate_button)
        assert counters.is_displayed(SelectedAddress.fixed_button)
        assert counters.is_displayed(SelectedAddress.init_values_button)
        assert counters.is_displayed(SelectedAddress.new_value_button)

    def teardown(self):
        self.driver.quit()

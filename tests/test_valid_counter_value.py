from selenium import webdriver
from src.PageObjects.login_page import Login
import time
from src.PageObjects.counters_page import Counters
from src.PageObjects.nav_menu import NavMenu


class TestValidCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_valid_counter_value(self):
        driver = self.driver
        counters = NavMenu(driver)
        counters.open_counters_page().choose_address().clickNewValueButton().setNewValue(-3)
        assert Counters.wrongMessagePresent()

        counters = NavMenu(driver)
        counters.open_counters_page().choose_address()
        value = Counters.get_current_value()
        Counters.clickNewValueButton().setNewValue(value + 1)
        time.sleep(7)
        counters.open_counters_page().choose_address()
        time.sleep(5)
        assert Counters.get_current_value() == value + 1

        counters = NavMenu(driver)
        counters.open_counters_page().choose_address().clickNewValueButton().setNewValue(123456789)
        assert Counters.wrongMessagePresent()


    def teardown(self):
        self.driver.quit()

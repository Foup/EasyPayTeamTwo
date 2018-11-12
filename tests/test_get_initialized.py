from src.locators import SelectedAddress
import time
from selenium import webdriver
from src.PageObjects.login_page import Login
from src.PageObjects.nav_menu import NavMenu
import psycopg2


'''Verify that the specific address from the list can be chosen
 and buttons “activate/deactivate”, “set fixed/unfixed”,
 “set initial value” and “set new value” are displayed'''


class TestGetCounterInitialized:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()
        conn = psycopg2.connect(dbname="easypay_db", user="postgres",
                                password="postgres", host="localhost")
        cursor = conn.cursor()
        with cursor.execute("UPDATE counters SET old_value = 0,"
                            " current_value = 0 WHERE id = 49;"), conn.commit():
            print("Database was successfully updated")

    def test_get_initialized(self):
        driver = self.driver
        counters = NavMenu(driver)
        counter = counters.open_counters_page() \
            .choose_address()
        assert counter.is_button_enabled(SelectedAddress.init_values_button)
        counter.init_values()
        time.sleep(10)
        counter.choose_address() \
            .waitForElement(SelectedAddress.current_value)
        assert counter.get_current_value() == 1

    def teardown(self):
        self.driver.quit()

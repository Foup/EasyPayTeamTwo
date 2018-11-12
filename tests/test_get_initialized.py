from src.locators import SelectedAddress
import time
from selenium import webdriver
from src.PageObjects.login_page import Login
from src.PageObjects.counters_page import Counters
import psycopg2


class TestGetCounterInitialized:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()
        conn = psycopg2.connect(dbname="easypay_db", user="postgres", password="postgres", host="localhost")
        cursor = conn.cursor()
        cursor.execute("UPDATE counters SET old_value = 0, current_value = 0 WHERE id = 49;")
        conn.commit()
        conn.close()

    def test_get_initialized(self):
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address()
        assert counters.getElement(SelectedAddress
                                   .init_values_button).is_enabled()
        counters.init_values()
        time.sleep(10)
        counters.choose_address()\
            .waitForElement(SelectedAddress.current_value)
        assert int(counters.getElement(SelectedAddress.current_value)
                   .get_attribute('data-value')) == 1

    def teardown(self):
        self.driver.quit()

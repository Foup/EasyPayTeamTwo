from selenium import webdriver
from src.PageObjects.login_page import Login
from src.PageObjects.counters_page import Counters
from src.db_conn import DBConnection

class TestCounterActiveValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_counter_active_value(self):
        with DBConnection() as db:
            db.set_deactivated()
            print("Database was successfully updated")
        counters = Counters(self.driver)
        counters.open_counters_page()\
            .choose_address()\
            .change_active_status()
        with DBConnection() as db:
            assert db.check_status_active()

    def test_counter_active_value(self):
        with DBConnection() as db:
            db.set_activated()
            print("Database was successfully updated")
        counters = Counters(self.driver)\
            .open_counters_page()\
            .choose_address()\
            .change_active_status()
        with DBConnection() as db:
            assert not db.check_status_active()

    def teardown(self):
        self.driver.quit()
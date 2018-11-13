from selenium import webdriver

from src.PageObjects.counters_page import Counters
from src.PageObjects.login_page import Login
from src.db_conn import DBConnection


class TestValidCounterValue:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_fix_value(self):
        with DBConnection() as db:
            db.set_unfixed()
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address().change_fix_status()
        with DBConnection() as db:
            assert db.check_status_fix()

    def test_unfix_value(self):
        with DBConnection() as db:
            db.set_fixed()
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address().change_fix_status()
        with DBConnection() as db:
            assert not db.check_status_fix()

    def teardown(self):
        self.driver.quit()

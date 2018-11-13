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
        DBConnection.set_fixed()
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address().change_fix_status()
        status = DBConnection.check_status_fix()
        assert status =="FALSE"

    def test_unfix_value(self):
        DBConnection.set_unfixed()
        driver = self.driver
        counters = Counters(driver)
        counters.open_counters_page() \
            .choose_address().change_fix_status()
        status = DBConnection.check_status_fix()
        assert status =="TRUE"

    def teardown(self):
        self.driver.quit()

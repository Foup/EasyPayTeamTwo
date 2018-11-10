from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import PathToCounters
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.PageObjects.Login_Page import Login


class TestAddressesAvailable:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()

    def test_addresses_available(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        self.driver.find_element(By.XPATH, PathToCounters.counters_menu_item).click()
        self.driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'x_panel')))
        assert self.driver.find_element(By.XPATH, PathToCounters.counters_addresses_list).is_displayed()
        time.sleep(2)

    def teardown(self):
        self.driver.quit()



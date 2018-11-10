from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.locators import PathToCounters
from src.locators import SelectedAddress
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.PageObjects.login_page import Login
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
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.address_li).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.init_values_button)))
        assert driver.find_element(By.XPATH, SelectedAddress.init_values_button).is_enabled()
        driver.find_element(By.XPATH, SelectedAddress.init_values_button).click()
        time.sleep(10)
        driver.find_element(By.XPATH, PathToCounters.dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.address_li).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, SelectedAddress.current_value)))
        assert int(driver.find_element(By.XPATH, SelectedAddress.current_value)
                   .get_attribute('data-value')) == 1

    def teardown(self):
        self.driver.quit()

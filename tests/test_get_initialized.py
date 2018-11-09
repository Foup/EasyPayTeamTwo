from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from src.Locators import PathToCounters
from src.Locators import SelectedAddress
from src.Locators import NewValue
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.PageObjects.Login_Page import Login
import psycopg2


class TestGetCounterInitialized:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        login = Login(driver)
        login.login_as_inspector()
        conn = psycopg2.connect(dbname="easypay_db", user="postgres", password="300691", host="localhost")
        cursor = conn.cursor()
        cursor.execute("UPDATE counters SET old_value = 0, current_value = 0 WHERE id = 49;")
        conn.commit()
        conn.close()

    def test_get_initialized(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.counters_menu_item).click()
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, SelectedAddress.counters_init_values_button)))
        assert driver.find_element(By.XPATH, SelectedAddress.counters_init_values_button).is_enabled()
        driver.find_element(By.XPATH, SelectedAddress.counters_init_values_button).click()
        time.sleep(10)
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, SelectedAddress.counters_current_value)))
        assert int(driver.find_element(By.XPATH, SelectedAddress.counters_current_value)
                   .get_attribute('data-value')) == 1

    def teardown(self):
        self.driver.quit()

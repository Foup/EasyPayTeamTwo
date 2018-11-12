from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from src.locators import HomePage, PathToCounters
from src.PageObjects.page import Page


class Counters(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def open_counters_page(self):
        self.driver.find_element(By.XPATH, PathToCounters.menu_item).click()
        return self

    def expand_counters_dropdown(self):
        self.driver.find_element(By.XPATH, PathToCounters.dropdown).click()
        return self

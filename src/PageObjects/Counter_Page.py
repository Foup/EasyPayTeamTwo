from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.Locators import PathToCounters


class OpenCounterPage:

    def CounterPage(driver):
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, 'display-name')))
        driver.find_element(By.XPATH, PathToCounters.counters_menu_item).click()
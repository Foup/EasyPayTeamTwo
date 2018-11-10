from src.Locators import PathToCounters
from selenium.webdriver.common.by import By



class GetAddress:
    def ChooseAddress(driver):
        driver.find_element(By.XPATH, PathToCounters.counters_dropdown).click()
        driver.find_element(By.XPATH, PathToCounters.counters_address_li).click()
        return driver
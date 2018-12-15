from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from src.url import login_page


class WebdriverFactory:

    def __init__(self, browser, base_url=login_page):
        self.browser = browser
        self.base_url = base_url

    def get_webdriver_instance(self):
        browser = self.browser.lower()
        if browser == 'firefox':
            driver = self.get_firefox_driver()
        elif browser == 'chrome':
            driver = self.get_chrome_driver()
        elif browser == 'edge':
            driver = self.get_edge_driver()
        elif browser == 'opera':
            driver = self.get_opera_driver()
        else:
            print("Browser: %s not supported!" % browser)
            raise NotImplementedError
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(self.base_url)
        return driver

    def get_chrome_driver(self):
        return webdriver.Remote("http://localhost:4444/wd/hub",
                                DesiredCapabilities.CHROME)

    def get_firefox_driver(self):
        return webdriver.Firefox()

    def get_edge_driver(self):
        return webdriver.Edge()

    def get_opera_driver(self):
        return webdriver.Opera()

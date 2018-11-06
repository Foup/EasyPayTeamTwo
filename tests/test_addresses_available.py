from selenium import webdriver


class TestAddressesAvailable:

    def setup(self):
        self.driver = webdriver.Chrome()
        driver = self.driver


    def test_addresses_available(self):
        pass

    def teardown(self):
        self.driver.quit()



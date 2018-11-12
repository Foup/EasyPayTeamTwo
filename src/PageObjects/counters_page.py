from src.locators import HomePage, PathToCounters, SelectedAddress
from src.PageObjects.page import Page


class Counters(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.waitForElement(HomePage.display_name)

    def open_counters_page(self):
        self.clickOnElement(PathToCounters.menu_item)\
            .waitForElement(PathToCounters.panel)
        return self

    def expand_counters_dropdown(self):
        self.clickOnElement(PathToCounters.dropdown)\
            .waitForElement(PathToCounters.addresses_list)
        return self

    def choose_address(self):
        return self.expand_counters_dropdown()\
            .clickOnElement(PathToCounters.address_li)\
            .waitForElement(SelectedAddress.table_body)

    def is_displayed(self, element):
        return self.isElementPresent(element)

    def init_values(self):
        return self.clickOnElement(SelectedAddress.init_values_button)

    def get_current_value(self):
        return int(self.getElement(SelectedAddress.current_value)
                   .get_attribute('data-value'))

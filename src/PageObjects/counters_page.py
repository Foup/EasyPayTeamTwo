from src.locators import HomePage, PathToCounters
from src.PageObjects.page import Page


class Counters(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def open_counters_page(self):
        self.clickOnElement(PathToCounters.menu_item)
        return self

    def expand_counters_dropdown(self):
        self.clickOnElement(PathToCounters.dropdown)
        return self

    def choose_address(self):
        return self.waitForElement(HomePage.display_name)\
            .open_counters_page() \
            .waitForElement(PathToCounters.panel)\
            .expand_counters_dropdown()

    def addresses_list_presented(self):
        return self.isElementPresent(PathToCounters.addresses_list)

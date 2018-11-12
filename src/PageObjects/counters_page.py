from src.locators import HomePage, PathToCounters, SelectedAddress, NewValue
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

    def init_values(self):
        return self.clickOnElement(SelectedAddress.init_values_button)

    def get_current_value(self):
       return int(self.getElement(SelectedAddress.current_value)
                   .get_attribute('data-value'))

    def clickNewValueButton(self):
        self.driver.waitForElement(SelectedAddress.new_value_button)\
            .clickOnElement(SelectedAddress.new_value_button)

    def setNewValue(self, value):
        self.driver.clickOnElement(NewValue.field).clear()\
            .sendKeysToElement(value, NewValue.field)\
            .clickOnElement(NewValue.apply_button)

    def wrongMessagePresent(self):
         self.driver.is_displayed(NewValue.wrong_value_message)
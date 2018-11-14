from src.locators import HomePage, PathToCounters, SelectedAddress, NewValue
from src.PageObjects.page import Page
from src.Utilities.logger import logger


class Counters(Page):

    log = logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element(HomePage.display_name)

    def open_counters_page(self):
        self.click_on_element(PathToCounters.menu_item)\
            .wait_for_element(PathToCounters.panel)
        return self

    def expand_counters_dropdown(self):
        self.click_on_element(PathToCounters.dropdown)\
            .wait_for_element(PathToCounters.addresses_list)
        return self

    def choose_address(self):
        return self.expand_counters_dropdown()\
            .click_on_element(PathToCounters.address_li)\
            .wait_for_element(SelectedAddress.table_body)

    def init_values(self):
        return self.click_on_element(SelectedAddress.init_values_button)

    def get_current_value(self):
        return int(self.get_element(SelectedAddress.current_value)
                   .get_attribute('data-value'))

    def get_old_value(self):
        return int(self.get_element(SelectedAddress.old_value).text)

    def open_new_value_modal(self):
        self.click_on_element(SelectedAddress.new_value_button)\
            .wait_for_element(NewValue.label)\
            .wait_for_element(NewValue.field)
        return self

    def set_new_value(self, value):
        self.send_keys_to_element(str(value), NewValue.field)\
            .click_on_element(NewValue.apply_button)
        return self

    def change_fix_status(self):
        self.click_on_element(SelectedAddress.fixed_button)

    def change_active_status(self):
        self.click_on_element(SelectedAddress.activate_button)

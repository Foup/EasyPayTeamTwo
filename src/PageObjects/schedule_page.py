from src.locators import HomePage, PathToInspectors, \
    AddScheduleItem, EditScheduleItem, DeleteScheduleItem, Navigation, Route
from src.PageObjects.page import Page
from src.Utilities.logger import logger


class Schedule(Page):
    log = logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element(HomePage.display_name)

    def open_inspectors_page(self):
        self.click_on_element(PathToInspectors.menu_item)

    def open_schedule_page(self):
        self.click_on_element(PathToInspectors.menu_item) \
            .wait_for_element(PathToInspectors.inspector) \
            .click_on_element(PathToInspectors.inspector) \
            .wait_for_element(AddScheduleItem.add_schedule_item_button)
        return self

    def open_add_schedule_item_modal(self):
        self.click_on_element(AddScheduleItem.add_schedule_item_button) \
            .wait_for_element(AddScheduleItem.choose_data_edit)
        return self

    def choose_date_in_modal_add(self, data):
        self.click_on_element(AddScheduleItem.choose_data_edit) \
            .send_keys_to_element(str(data), AddScheduleItem.choose_data_edit)
        return self

    def choose_address_in_modal_add(self):
        self.click_on_element(AddScheduleItem.dropdown_list_addresses) \
            .click_on_element(AddScheduleItem.address_chosen)
        return self

    def repeat_every_month_add(self):
        self.click_on_element(AddScheduleItem.repeat_every_month_checkbox)
        return self

    def warning_in_add_modal(self):
        self.is_displayed(AddScheduleItem.no_address_set_warning)
        return self

    def add_schedule_item(self):
        self.click_on_element(AddScheduleItem.apply_button)
        return self

    def open_edit_schedule_item_modal(self):
        self.click_on_element(EditScheduleItem.edit_button) \
            .wait_for_element(EditScheduleItem.address_chosen)
        return self

    def choose_date_in_modal_edit(self, data):
        self.click_on_element(EditScheduleItem.address_chosen) \
            .send_keys_to_element(str(data), EditScheduleItem.address_chosen)
        return self

    def choose_address_in_modal_edit(self):
        self.click_on_element(EditScheduleItem.remove_address) \
            .click_on_element(EditScheduleItem.dropdown_list_addresses) \
            .click_on_element(EditScheduleItem.address_chosen)
        return self

    def repeat_every_month_edit(self):
        self.click_on_element(EditScheduleItem.repeat_every_month_checkbox)
        return self

    def warning_in_edit_modal(self):
        self.is_displayed(EditScheduleItem.no_address_set_warning)
        return self

    def edit_schedule_item(self):
        self.click_on_element(EditScheduleItem.apply_button)

    def delete_schedule_item_modal(self):
        self.click_on_element(DeleteScheduleItem.delete_button) \
            .wait_for_element(DeleteScheduleItem.modal_window)
        return self

    def delete_schedule_item(self):
        self.click_on_element(DeleteScheduleItem.apply_button)
        return self

    def schedule_route(self):
        self.click_on_element(Route.route_button)
        return self

    def navigate_to_next_month(self):
        self.click_on_element(Navigation.navigation_next_month)
        return self

    def navigate_to_prev_month(self):
        self.click_on_element(Navigation.navigation_prev_month)
        return self

    def navigate_today(self):
        self.click_on_element(Navigation.navigation_today)
        return self
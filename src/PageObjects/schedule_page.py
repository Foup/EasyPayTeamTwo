import time

from src.locators import HomePage, PathToInspectors, \
    AddScheduleItem, EditScheduleItem, DeleteScheduleItem, Navigation, Route, \
    ManagerSchedule
from src.PageObjects.page import Page
from src.Utilities.logger import logger
from src.test_data import address_for_schedule


class Schedule(Page):
    log = logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element(HomePage.display_name)

    def open_inspectors_page(self):
        self.click_on_element(PathToInspectors.menu_item)\
            .wait_for_element(PathToInspectors.inspector)
        return self

    def open_schedule_page(self):
        self.click_on_element(PathToInspectors.inspector) \
            .wait_for_element(ManagerSchedule.add_schedule_item_button)
        return self

    def open_add_schedule_item_modal(self):
        self.click_on_element(ManagerSchedule.add_schedule_item_button) \
            .wait_for_element(AddScheduleItem.choose_data_edit)
        return self

    def choose_date_in_modal_add(self, data):
        from selenium.webdriver.common.keys import Keys
        self.wait_for_element(AddScheduleItem.choose_data_edit)\
            .click_on_element(AddScheduleItem.choose_data_edit)\
            .send_keys_to_element(8 * Keys.BACK_SPACE,
                                  AddScheduleItem.choose_data_edit)
        time.sleep(2)
        self.send_keys_to_element(data, AddScheduleItem.choose_data_edit)
        return self

    def choose_address_in_modal_add(self):
        self.click_on_element(AddScheduleItem.address_dropdown)
        self.send_keys_to_element(address_for_schedule,
                                  AddScheduleItem.address_dropdown)
        self.click_on_element(AddScheduleItem.address_chosen)
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

    def is_add_task_button_enabled(self):
        return self.is_button_enabled(AddScheduleItem.apply_button)

    def open_edit_schedule_item_modal(self):
        self.click_on_element(ManagerSchedule.edit_button) \
            .wait_for_element(EditScheduleItem.apply_button)
        return self

    def choose_date_in_modal_edit(self, data):
        from selenium.webdriver.common.keys import Keys
        self.wait_for_element(EditScheduleItem.edit_data) \
            .send_keys_to_element(8 * Keys.BACK_SPACE,
                                  EditScheduleItem.edit_data)
        self.send_keys_to_element(data, EditScheduleItem.edit_data)
        return self

    def is_element_in_schedule(self, date):
        return self.is_element_present(EditScheduleItem.is_element_present % date)

    def choose_address_in_modal_edit(self):
        self.click_on_element(EditScheduleItem.remove_address) \
            .click_on_element(EditScheduleItem.dropdown_list_addresses) \
            .click_on_element(EditScheduleItem.address_chosen)
        return self

    def repeat_every_month_edit(self):
        self.click_on_element(EditScheduleItem.repeat_every_month_checkbox)
        return self

    def is_displayed_warning(self):
        return self.is_displayed(EditScheduleItem.no_address_set_warning)

    def edit_schedule_item(self):
        self.click_on_element(EditScheduleItem.apply_button)\
            .wait_for_element_disappear(EditScheduleItem.apply_button)
        return self

    def delete_schedule_item_modal(self):
        self.click_on_element(ManagerSchedule.delete_button)
        self.wait_for_element(DeleteScheduleItem.modal_window)
        return self

    def delete_schedule_item(self):
        self.click_on_element(DeleteScheduleItem.apply_button)\
            .wait_for_element_disappear(DeleteScheduleItem.apply_button)
        return self

    def schedule_route(self):
        self.click_on_element(Route.route_button)
        return self

    def navigate_to_next_month(self):
        self.click_on_element(Navigation.next_month)
        return self

    def navigate_to_prev_month(self):
        self.click_on_element(Navigation.prev_month)
        return self

    def navigate_today(self):
        self.click_on_element(Navigation.today)
        return self

    def close_modal_add(self):
        self.click_on_element(AddScheduleItem.close)\
            .wait_for_element_disappear(AddScheduleItem.close)
        return self

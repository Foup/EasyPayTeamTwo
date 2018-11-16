import allure

from src.PageObjects.schedule_page import Schedule
from src.locators import AddScheduleItem


def test_add_task_without_address(manager_setup):
    inspector = Schedule(manager_setup)\
        .open_inspectors_page()\
        .open_schedule_page()
    inspector.open_add_schedule_item_modal()
    with allure.step("Verify button enabled"):
        assert inspector.is_button_enabled(AddScheduleItem.apply_button), \
            "Button disabled"
    inspector.add_schedule_item()\
        .wait_for_element(AddScheduleItem.no_address_set_warning)
    assert inspector.is_displayed_warning()
    inspector.close_modal_add()


def test_add_task(manager_setup):
    inspector = Schedule(manager_setup) \
        .open_inspectors_page() \
        .open_schedule_page()
    inspector.open_add_schedule_item_modal()\
        .choose_address_in_modal_add()
    assert inspector.is_button_enabled(AddScheduleItem.apply_button)
    inspector.add_schedule_item()

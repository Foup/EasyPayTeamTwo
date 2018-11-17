import allure

from src.PageObjects.schedule_page import Schedule
from src.locators import AddScheduleItem


def test_add_task_without_address(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    schedule.open_add_schedule_item_modal()
    with allure.step("Verify button enabled"):
        assert schedule.is_button_enabled(AddScheduleItem.apply_button), \
            "Button disabled"
    schedule.add_schedule_item()\
        .wait_for_element(AddScheduleItem.no_address_set_warning)
    assert schedule.is_displayed_warning()
    schedule.close_modal_add()


def test_add_task(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    schedule.open_add_schedule_item_modal()\
        .choose_address_in_modal_add()
    assert schedule.is_button_enabled(AddScheduleItem.apply_button)
    schedule.add_schedule_item()

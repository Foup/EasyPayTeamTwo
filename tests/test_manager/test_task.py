import time

import allure

from src.locators import AddScheduleItem, ManagerSchedule, EditScheduleItem


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


def test_edit_task_address(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    schedule.open_edit_schedule_item_modal()
    with allure.step("Verify button enabled"):
        assert schedule.is_button_enabled(ManagerSchedule.edit_button), \
            "Button disabled"
    schedule.choose_date_in_modal_edit('2018-11-26')\
        .choose_address_in_modal_edit().edit_schedule_item()
    assert not schedule.is_element_present(EditScheduleItem.edit_modal)
    time.sleep(4)

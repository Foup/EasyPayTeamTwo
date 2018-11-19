import allure

from src.locators import AddScheduleItem
from src.test_data import schedule_item_date, schedule_item_date_27


def test_add_task_without_address(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    schedule.open_add_schedule_item_modal()
    with allure.step("Verify apply button is enabled"):
        assert schedule.is_button_enabled(AddScheduleItem.apply_button), \
            "Button disabled"
    schedule.add_schedule_item()
    with allure.step("Verify there is warning message in case no address"):
        assert schedule.is_displayed_warning(), "No warning message"
    schedule.close_modal_add()


def test_add_task(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    schedule.open_add_schedule_item_modal()\
        .choose_address_in_modal_add()
    schedule.choose_date_in_modal_add(schedule_item_date)
    with allure.step("Verify apply button is enabled"):
        assert schedule.is_add_task_button_enabled(), "Button is disabled"
    schedule.add_schedule_item()
    with allure.step("Verify that task was added"):
        assert schedule.is_element_in_schedule(schedule_item_date), \
            "Task wasn't added"


def test_edit_task_address(schedule_one_new_value_27_setup,
                           get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    with allure.step("Verify there is no tasks on that day"):
        assert not schedule.is_element_in_schedule(schedule_item_date)
        schedule.open_edit_schedule_item_modal()\
            .choose_date_in_modal_edit(schedule_item_date).edit_schedule_item()
    with allure.step("Verify task edited"):
        assert schedule.is_element_in_schedule(schedule_item_date)
        assert not schedule.is_element_in_schedule(schedule_item_date_27)


def test_address_deletion(schedule_one_new_value_setup,
                          get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager\
        .delete_schedule_item_modal()\
        .delete_schedule_item()
    with allure.step("Verify there is no task on that day"):
        assert not schedule.is_element_in_schedule(schedule_item_date)

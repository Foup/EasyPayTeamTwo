from src.PageObjects.nav_menu import NavMenu
from src.locators import ManagerSchedule, AddScheduleItem


def test_add_task_without_address(manager_setup):
    inspector = NavMenu(manager_setup).open_inspector_page()
    inspector.open_schedule_page()
    inspector.click_on_element(ManagerSchedule.add_schedule_item_button)
    assert inspector.is_button_enabled(AddScheduleItem.apply_button)
    inspector.click_on_element(AddScheduleItem.apply_button)
    assert inspector.is_displayed(AddScheduleItem.no_address_set_warning)

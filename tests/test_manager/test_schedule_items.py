from src.PageObjects.nav_menu import NavMenu
from src.locators import Navigation, ManagerSchedule

def test_address_deletion(manager_setup, schedule_new_value_setup):
    schedule = NavMenu(manager_setup).open_inspector_page()\
        .open_schedule_page()\
        .delete_schedule_item_modal()\
        .delete_schedule_item()\



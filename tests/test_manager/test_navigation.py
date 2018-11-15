from src.PageObjects.nav_menu import NavMenu
from src.locators import Navigation, ManagerSchedule


def test_next_prev_month(manager_setup):
    inspector = NavMenu(manager_setup).open_inspector_page()
    inspector.open_schedule_page()
    assert inspector.is_button_enabled(Navigation.next_month, 'css')
    assert not inspector.is_button_enabled(Navigation.prev_month, 'css')
    inspector.click_on_element(Navigation.next_month, 'css')
    assert not inspector.is_button_enabled(Navigation.next_month, 'css')
    assert inspector.is_button_enabled(Navigation.prev_month, 'css')
    inspector.click_on_element(Navigation.prev_month, 'css')
    assert inspector.is_button_enabled(ManagerSchedule.add_schedule_item_button)


def test_navigate_today(manager_setup):
    inspector = NavMenu(manager_setup).open_inspector_page()
    inspector.open_schedule_page()
    assert not inspector.is_button_enabled(Navigation.today)
    inspector.click_on_element(Navigation.next_month, 'css')
    assert inspector.is_button_enabled(Navigation.today)

from src.locators import Navigation, ManagerSchedule


def test_next_prev_month(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    assert schedule.is_button_enabled(Navigation.next_month, 'css')
    assert not schedule.is_button_enabled(Navigation.prev_month, 'css')
    schedule.click_on_element(Navigation.next_month, 'css')
    assert not schedule.is_button_enabled(Navigation.next_month, 'css')
    assert schedule.is_button_enabled(Navigation.prev_month, 'css')
    schedule.click_on_element(Navigation.prev_month, 'css')
    assert schedule.is_button_enabled(ManagerSchedule.add_schedule_item_button)


def test_navigate_today(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    assert not schedule.is_button_enabled(Navigation.today)
    schedule.click_on_element(Navigation.next_month, 'css')
    assert schedule.is_button_enabled(Navigation.today)

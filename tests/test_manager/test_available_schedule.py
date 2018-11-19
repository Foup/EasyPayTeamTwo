import allure

from src.locators import ManagerSchedule


def test_available_schedule(get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager
    with allure.step("Verify schedule is visible"):
        assert schedule.is_displayed(ManagerSchedule.schedule)

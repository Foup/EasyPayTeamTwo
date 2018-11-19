from src.locators import ManagerSchedule


def test_address_deletion(schedule_new_value_setup,
                          get_inspector_schedule_from_manager):
    schedule = get_inspector_schedule_from_manager\
        .delete_schedule_item_modal()\
        .delete_schedule_item()
    assert not schedule.is_displayed(ManagerSchedule.route)

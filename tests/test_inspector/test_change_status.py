import time

from src.db_conn import DBConnection
from src.locators import SelectedAddress


def test_counter_activated_value(inspector_setup):
    with DBConnection() as db:
        db.set_deactivated()
        print("Database was successfully updated")
    counters = inspector_setup
    counters.open_counters_page() \
        .choose_address() \
        .change_active_status()
    with DBConnection() as db:
        assert db.check_status_active()


def test_counter_deactivated_value(inspector_setup):
    with DBConnection() as db:
        db.set_activated()
        print("Database was successfully updated")
    counters = inspector_setup
    counters.open_counters_page() \
        .choose_address() \
        .change_active_status()
    with DBConnection() as db:
        assert not db.check_status_active()


def test_fix_value(inspector_setup):
    with DBConnection() as db:
        db.set_unfixed()
    counters = inspector_setup
    counters.open_counters_page() \
        .choose_address().change_fix_status()
    with DBConnection() as db:
        assert db.check_status_fix()


def test_unfix_value(inspector_setup):
    with DBConnection() as db:
        db.set_fixed()
    counters = inspector_setup
    counters.open_counters_page() \
        .choose_address().change_fix_status()
    with DBConnection() as db:
        assert not db.check_status_fix()


def test_get_initialized(inspector_setup):
    with DBConnection() as db:
        db.set_zero_values()
        print("Database was successfully updated")
    counters = inspector_setup
    counter = counters.open_counters_page() \
        .choose_address()
    assert counter.is_button_enabled(SelectedAddress.init_values_button)
    counter.init_values()
    time.sleep(10)
    counter.choose_address() \
        .wait_for_element(SelectedAddress.current_value)
    assert counter.get_current_value() == 1

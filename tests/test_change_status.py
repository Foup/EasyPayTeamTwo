from src.PageObjects.counters_page import Counters
from src.PageObjects.nav_menu import NavMenu
from src.db_conn import DBConnection
from src.locators import SelectedAddress
import time


def test_counter_activated_value(resource_setup):
    with DBConnection() as db:
        db.set_deactivated()
        print("Database was successfully updated")
    counters = Counters(resource_setup)
    counters.open_counters_page() \
        .choose_address() \
        .change_active_status()
    with DBConnection() as db:
        assert db.check_status_active()


def test_counter_deactivated_value(resource_setup):
    with DBConnection() as db:
        db.set_activated()
        print("Database was successfully updated")
    counters = Counters(resource_setup)
    counters.open_counters_page() \
        .choose_address() \
        .change_active_status()
    with DBConnection() as db:
        assert not db.check_status_active()


def test_fix_value(resource_setup):
    with DBConnection() as db:
        db.set_unfixed()
    counters = Counters(resource_setup)
    counters.open_counters_page() \
        .choose_address().change_fix_status()
    with DBConnection() as db:
        assert db.check_status_fix()


def test_unfix_value(resource_setup):
    with DBConnection() as db:
        db.set_fixed()
    counters = Counters(resource_setup)
    counters.open_counters_page() \
        .choose_address().change_fix_status()
    with DBConnection() as db:
        assert not db.check_status_fix()


def test_get_initialized(resource_setup):
    with DBConnection() as db:
        db.set_zero_values()
        print("Database was successfully updated")
    counters = NavMenu(resource_setup)
    counter = counters.open_counters_page() \
        .choose_address()
    assert counter.is_button_enabled(SelectedAddress.init_values_button)
    counter.init_values()
    time.sleep(10)
    counter.choose_address() \
        .wait_for_element(SelectedAddress.current_value)
    assert counter.get_current_value() == 1

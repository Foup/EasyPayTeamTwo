import time

import allure
import pytest

from src.PageObjects.nav_menu import NavMenu
from src.locators import NewValue
from src.db_conn import DBConnection

''' Verify that it is a warning message
when new value is less than previous.'''


def test_new_counter_value(inspector_setup):
    counters = NavMenu(inspector_setup)
    counters = counters.open_counters_page() \
        .choose_address()
    value = counters.get_current_value()
    counters.open_new_value_modal() \
        .set_new_value(value + 1)
    time.sleep(10)
    counters.choose_address()
    assert counters.get_current_value() == value + 1


def test_valid_counter_value(inspector_setup):
    counters = NavMenu(inspector_setup)
    counters = counters.open_counters_page() \
        .choose_address()
    value = counters.get_current_value()
    counters.open_new_value_modal() \
        .set_new_value(value + 1)
    time.sleep(10)
    counters.choose_address()
    assert counters.get_current_value() == value + 1


@pytest.mark.parametrize('value', (-3, 123456789))
def test_invalid_counter_value(inspector_setup, value):
    counters = NavMenu(inspector_setup)
    counters.open_counters_page().choose_address().open_new_value_modal()\
        .set_new_value(value)
    with allure.step("Wrong message displayed"):
        assert counters.is_displayed(NewValue.wrong_value_message), \
            "No wrong message"
    counters.click_on_element(NewValue.close_button)


def test_less_value(inspector_setup):
    with DBConnection() as db:
        db.set_old_value()
        print("Database was successfully updated")
    counters = NavMenu(inspector_setup)
    counters = counters.open_counters_page() \
        .choose_address()
    old_value = counters.get_old_value()
    new_value = old_value - 5
    counters.open_new_value_modal() \
        .set_new_value(new_value)
    with allure.step("Modal window shows"):
        assert counters.is_displayed(NewValue.confirm_dialog), \
            "No modal window"
    counters.click_on_element(NewValue.close_button)

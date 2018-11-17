import time

import allure
import pytest

from src.locators import NewValue, SelectedAddress

''' Verify that it is a warning message
when new value is less than previous.'''


def test_new_counter_value(counter_new_value_setup, inspector_counter):
    counter = inspector_counter
    value = counter.get_current_value()
    counter.open_new_value_modal() \
        .set_new_value(value + 1)
    assert counter.is_displayed(SelectedAddress.notify) == False
    time.sleep(5)
    counter.choose_address()
    assert counter.get_current_value() == value + 1


def test_valid_counter_value(counter_new_value_setup, inspector_counter):
    counter = inspector_counter
    value = counter.get_current_value()
    counter.open_new_value_modal() \
        .set_new_value(value + 1)
    time.sleep(10)
    counter.choose_address()
    assert counter.get_current_value() == value + 1


@pytest.mark.parametrize('value', (-3, 123456789))
def test_invalid_counter_value(counter_new_value_setup,
                               inspector_counter, value):
    counter = inspector_counter
    counter.open_new_value_modal()
    counter.set_new_value(value)
    with allure.step("Wrong message displayed"):
        assert counter.is_displayed(NewValue.wrong_value_message), \
            "No wrong message"
    counter.click_on_element(NewValue.close_button)


def test_less_value(counter_new_value_setup, inspector_counter):
    counter = inspector_counter
    old_value = counter.get_old_value()
    new_value = old_value - 5
    counter.open_new_value_modal() \
        .set_new_value(new_value)
    with allure.step("Modal window shows"):
        assert counter.is_displayed(NewValue.confirm_dialog), \
            "No modal window"
    counter.click_on_element(NewValue.close_button)

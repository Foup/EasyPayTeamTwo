import allure

from src.locators import PathToCounters, SelectedAddress


''' Verify that the list of clients addresses assigned
 to the inspector is available.'''


def test_addresses_available(inspector_setup):
    counters = inspector_setup
    counters.open_counters_page() \
        .expand_counters_dropdown()
    with allure.step("Addresses list displayed"):
        assert counters.is_displayed(PathToCounters.addresses_list), \
            "Addresses list not displayed"


def test_select_counter(inspector_counter):
    counters = inspector_counter
    with allure.step("Counter info displayed"):
        assert counters.is_displayed(SelectedAddress.utility), \
            "Utility not displayed"
        assert counters.is_displayed(SelectedAddress.old_value), \
            "Old value not displayed"
        assert counters.is_displayed(SelectedAddress.current_value), \
            "Current value not displayed"
        assert counters.is_displayed(SelectedAddress.activate_button), \
            "Activate/deactivate button not displayed"
        assert counters.is_displayed(SelectedAddress.fixed_button), \
            "Fix/unfix button not displayed"
        assert counters.is_displayed(SelectedAddress.init_values_button), \
            "Init values button not displayed"
        assert counters.is_displayed(SelectedAddress.new_value_button), \
            "New value button not displayed"

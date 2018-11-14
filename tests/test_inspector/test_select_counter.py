from src.PageObjects.nav_menu import NavMenu
from src.locators import PathToCounters, SelectedAddress


''' Verify that the list of clients addresses assigned
 to the inspector is available.'''


def test_addresses_available(inspector_setup):
    counters = NavMenu(inspector_setup)
    counters.open_counters_page() \
        .expand_counters_dropdown()
    assert counters.is_displayed(PathToCounters.addresses_list)


def test_select_counter(inspector_setup):
    counters = NavMenu(inspector_setup)
    counters.open_counters_page() \
        .choose_address()
    assert counters.is_displayed(SelectedAddress.utility)
    assert counters.is_displayed(SelectedAddress.old_value)
    assert counters.is_displayed(SelectedAddress.current_value)
    assert counters.is_displayed(SelectedAddress.activate_button)
    assert counters.is_displayed(SelectedAddress.fixed_button)
    assert counters.is_displayed(SelectedAddress.init_values_button)
    assert counters.is_displayed(SelectedAddress.new_value_button)

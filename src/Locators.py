from src import Params


class PathToCounters(object):
    counters_menu_item = '//*[@id="sidebar-menu"]/div/ul/li[2]/a/span'
    counters_dropdown = '//*[@class="input-group-addon dropdown-toggle"]'
    counters_addresses_list = '//ul[@class="typeahead typeahead-long dropdown-menu"]'
    counters_address_li = '//li[@data-value="' + Params.address + '"]'
    panel = '//div[@class="x_panel"]'


class SelectedAddress(object):
    counters_table = '//table[@id="countersTable"]'
    counters_utility = '//*[@id="countersTable"]//td[contains(text(),"' + Params.utility_name + '")]'
    counters_old_value = '//td[@class="oldValue"]'
    counters_current_value = '//td[@class="counter-value"]'
    counters_is_active_td = '//td[@class="is-active"]'
    counters_is_fixed_td = '//td[@class="is-fixed"]'
    counters_activate_button = '//button[@class="change-status btn btn-primary"]'
    counters_fixed_button = '//button[@class="change-type btn btn-primary"]'
    counters_fixed_button_label = '//*[@id="countersTable"]/tbody/tr/td[6]/button[2]'
    counters_init_values_button = '//button[@class="init-with-values btn btn-primary"]'
    counters_new_value_button = '//button[@class="btn btn-primary change-value"]'


class NewValue(object):
    new_value_label = '//h4[@id="myModalLabel"]'
    new_value_close = '//button[@class="close"]'
    new_value_field = '//input[@id="newCurrentValue"]'
    new_value_apply_button = '//button[@class="btn btn-primary js-apply"]'
    new_value_wrong_value_message = '//*[@id="wrong-value"]'
    new_value_close_button = '//button[@data-locale-item="close"]'
    # new_counter_value = '//*[@id="countersTable"]/tbody/tr/td[3]'

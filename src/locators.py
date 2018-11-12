from src import test_data


class HomePage(object):
    display_name = '//*[@id="display-name"]'


class PathToCounters(object):
    menu_item = '//*[@id="sidebar-menu"]/div/ul/li[2]/a/span'
    dropdown = '//*[@class="input-group-addon dropdown-toggle"]'
    addresses_list = '//ul[@class="typeahead typeahead-long dropdown-menu"]'
    address_li = '//li[@data-value="' + test_data.address + '"]'
    panel = '//div[@class="x_panel"]'


class SelectedAddress(object):
    table = '//table[@id="countersTable"]'
    table_body = '//*[@id="countersTable"]/tbody/tr'
    utility = '//*[@id="countersTable"]//td[contains(text(),"' +\
              test_data.utility_name + '")]'
    old_value = '//td[@class="oldValue"]'
    current_value = '//td[@class="counter-value"]'
    is_active_td = '//td[@class="is-active"]'
    is_fixed_td = '//td[@class="is-fixed"]'
    activate_button = '//button[@class="change-status btn btn-primary"]'
    fixed_button = '//button[@class="change-type btn btn-primary"]'
    init_values_button = '//button[@class="init-with-values btn btn-primary"]'
    new_value_button = '//button[@class="btn btn-primary change-value"]'


class NewValue(object):
    label = '//h4[@id="myModalLabel"]'
    close = '//button[@class="close"]'
    field = '//input[@id="newCurrentValue"]'
    apply_button = '//button[@class="btn btn-primary js-apply"]'
    wrong_value_message = '//*[@id="wrong-value"]'
    close_button = '//button[@data-locale-item="close"]'
    # new_counter_value = '//*[@id="countersTable"]/tbody/tr/td[3]'

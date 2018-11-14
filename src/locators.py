from src import test_data


class HomePage(object):
    display_name = '//*[@id="display-name"]'
    nav_menu = '//div[@class="menu_section"]'


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
    confirm_dialog = '//*[@id="confirm-dialog"]'
    close_button = '//button[@data-locale-item="close"]'


class PathToInspectors(object):
    menu_item = '//*[@id="sidebar-menu"]/div/ul/li[1]/a'
    inspector = '//*[@id="tab-inspectors"]/table/tbody/tr[1]/td[1]/a'


class Navigation(object):
    navigation_next_month = '//*[@id="manager-calendar"]/div[1]/div[1]/div/button[2]/span'
    navigation_prev_month = '//*[@id="manager-calendar"]/div[1]/div[1]/div/button[1]/span'
    navigation_today = '//*[@id="manager-calendar"]/div[1]/div[1]/button'


class DeleteScheduleItem(object):
    delete_button = '//*[@id="manager-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]' \
                    '/div[2]/table/tbody/tr/td[1]/button/i'
    apply_button = '//*[@id="remove-modal"]/div/div/div[3]/button[2]'
    close_button = '//*[@id="remove-modal"]/div/div/div[3]/button[1]/span'
    close = '//*[@id="remove-modal"]/div/div/div[1]/button/span'
    modal_window = '//*[@id="remove-modal"]/div/div/div[1]/h4'


class Route(object):
    route_button = '//*[@id="manager-calendar"]/div[2]/div/table/tbody/tr/td' \
                   '/div/div/div[3]/div[2]/table/thead/tr/td[4]/a'
    close = '//*[@id="map-modal"]/div/div/div[1]/button/span'


class EditScheduleItem(object):
    edit_button = '//*[@id="manager-calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/' \
                  'div[2]/table/tbody/tr/td[4]/a/div/i'
    edit_data = '//*[@id="datetimepicker-edit"]'
    remove_address = '//*[@id="edit-schedule-item-form"]/div/div/span/span[2]'
    dropdown_list_addresses = '//*[@id="edit-schedule-item-form"]/div/div/span'
    address_chosen = '//li[@data-value="' + test_data.edit_address_for_schedule + '"]'
    repeat_every_month_checkbox = '//*[@id="edit-schedule-item-form"]/span/small'
    close_button = '//*[@id="edit-modal"]/div/div/div[3]/button[1]/span'
    apply_button = '//*[@id="edit-modal"]/div/div/div[3]/button[2]/span'
    close = '//*[@id="edit-modal"]/div/div/div[1]/button/span'
    no_address_set_warning = '//*[@id="edit-schedule-item-form"]/ul[2]/li'


class AddScheduleItem(object):
    add_schedule_item_button = '//*[@id="manager-calendar"]/div[1]/div[2]/button'
    choose_data_edit = '//*[@id="datetimepicker"]'
    dropdown_list_addresses = '//*[@id="add-schedule-item-form"]/div/div/span'
    address_chosen = '//li[@data-value="' + test_data.address_for_schedule + '"]'
    repeat_every_month_checkbox = '//*[@id="add-schedule-item-form"]/span/small'
    close_button = '//*[@id="add-modal"]/div/div/div[3]/button[1]/span'
    apply_button = '//*[@id="add-modal"]/div/div/div[3]/button[2]/span'
    close = '//*[@id="add-modal"]/div/div/div[1]/button/span'
    no_address_set_warning = '//*[@id="add-schedule-item-form"]/ul[2]/li'

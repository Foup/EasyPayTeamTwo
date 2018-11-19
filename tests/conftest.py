from src.test_data import schedule_item_date, schedule_item_date_27, \
    schedule_item_id
from src.Base.webdriver_factory import WebdriverFactory
from src.PageObjects.login_page import Login
from src.PageObjects import page
from src.PageObjects.nav_menu import NavMenu

import pytest


@pytest.fixture(scope="function")
def get_driver(request, browser):
    driver = WebdriverFactory(browser).get_webdriver_instance()

    def close_driver():
        if request.node.rep_setup.failed:
            page.get_screenshot(driver,
                                "Setup %s failed" % request.function.__name__)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                page.get_screenshot(driver,
                                    "Setup %s failed"
                                    % request.function.__name__)
        driver.quit()
    request.addfinalizer(close_driver)
    return driver


@pytest.fixture(scope="function")
def inspector_setup(get_driver):
    driver = get_driver
    login = Login(driver)
    login.login_as_inspector()
    return NavMenu(driver)


@pytest.fixture(scope="function")
def manager_setup(get_driver):
    driver = get_driver
    login = Login(driver)
    login.login_as_manager()
    return NavMenu(driver)


@pytest.fixture(scope="function")
def inspector_counter(inspector_setup):
    return inspector_setup.open_counters_page()\
        .choose_address()


@pytest.fixture(scope="function")
def counter_new_value_setup():
    from src.db_conn import DBConnection
    with DBConnection() as db:
        db.get_ready_value()
        print("Database was successfully updated")


# add new item to the schedule
@pytest.fixture(scope="function")
def schedule_one_new_value_setup():
    from src.db_conn import DBConnection
    with DBConnection() as db:
        db.delete_schedule_item(schedule_item_date)
        db.delete_schedule_item(schedule_item_date_27)
        db.new_visit(schedule_item_date)
        print("Database was successfully updated")


@pytest.fixture(scope="function")
def schedule_one_new_value_27_setup():
    from src.db_conn import DBConnection
    with DBConnection() as db:
        db.delete_schedule_item(schedule_item_date)
        db.delete_schedule_item(schedule_item_date_27)
        db.new_visit(schedule_item_date_27)
        print("Database was successfully updated")


@pytest.fixture(scope="function")
def schedule_clear_setup():
    from src.db_conn import DBConnection
    with DBConnection() as db:
        db.delete_schedule_item(schedule_item_date)
        db.delete_schedule_item(schedule_item_date_27)
        print("Database was successfully updated")


@pytest.fixture(scope="function")
def get_inspector_schedule_from_manager(manager_setup):
    return manager_setup.open_inspector_page()\
        .open_schedule_page()


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

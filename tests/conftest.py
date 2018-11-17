from src import url
from src.Base.webdriver_factory import WebdriverFactory
from src.PageObjects.login_page import Login
from src.PageObjects import page
from src.PageObjects.counters_page import Counters

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
    return driver


@pytest.fixture(scope="function")
def manager_setup(get_driver):
    driver = get_driver
    login = Login(driver)
    return login.login_as_manager()


@pytest.fixture(scope="function")
def inspector_counter(inspector_setup):
    driver = inspector_setup
    return Counters(driver, url.counters_page).choose_address()


@pytest.fixture(scope="function")
def counter_new_value_setup():
    from src.db_conn import DBConnection
    with DBConnection() as db:
        db.get_ready_value()
        print("Database was successfully updated")


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

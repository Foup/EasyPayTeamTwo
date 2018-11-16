from src.Base.webdriver_factory import WebdriverFactory
from src.PageObjects.login_page import Login

import pytest


@pytest.fixture(scope="module")
def inspector_setup(request, browser):
    driver = WebdriverFactory(browser).get_webdriver_instance()
    login = Login(driver)
    login.login_as_inspector()

    def inspector_teardown():
        driver.quit()
    request.addfinalizer(inspector_teardown)
    return driver


@pytest.fixture(scope="module")
def manager_setup(request):
    driver = WebdriverFactory('Chrome').get_webdriver_instance()
    login = Login(driver)
    login.login_as_manager()

    def manager_teardown():
        driver.quit()
    request.addfinalizer(manager_teardown)
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

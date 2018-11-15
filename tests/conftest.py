from selenium import webdriver
from src.PageObjects.login_page import Login

import pytest


@pytest.fixture(scope="module")
def inspector_setup(request):
    driver = webdriver.Chrome()
    login = Login(driver)
    login.login_as_inspector()

    def inspector_teardown():
        driver.quit()
    request.addfinalizer(inspector_teardown)
    return driver


@pytest.fixture(scope="module")
def manager_setup(request):
    driver = webdriver.Chrome()
    login = Login(driver)
    login.login_as_manager()

    def manager_teardown():
        driver.quit()
    request.addfinalizer(manager_teardown)
    return driver

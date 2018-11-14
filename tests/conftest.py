from selenium import webdriver
from src.PageObjects.login_page import Login

import pytest


@pytest.fixture(scope="session")
def resource_setup(request):
    driver = webdriver.Chrome()
    login = Login(driver)
    login.login_as_inspector()

    def resource_teardown():
        driver.quit()
    request.addfinalizer(resource_teardown)
    return driver

from src import params


class User(object):
    def __init__(self, email=params.admin_email, password=params.admin_password):
        self.email = email
        self.password = password


def credentials(driver, user):
    driver.find_element_by_id('email').send_keys(user.email)
    driver.find_element_by_id('password').send_keys(user.password)


def login_by_role(get_credentials):
    def steps(driver):
        driver.get(params.url)
        driver.find_element_by_id('Sign_in').click()
        get_credentials(driver)
        credentials(driver, get_credentials(driver))
        driver.find_element_by_id('Login_button').click()
        driver.implicitly_wait(10)

    return steps


@login_by_role
def login_admin(driver):
    user = User(params.admin_email, params.admin_password)
    return user


@login_by_role
def login_inspector(driver):
    user = User(params.inspector_email, params.inspector_password)
    return user


@login_by_role
def login_manager(driver):
    user = User(params.manager_email, params.manager_password)
    return user


@login_by_role
def login_user(driver):
    user = User(params.user_email, params.user_password)
    return user
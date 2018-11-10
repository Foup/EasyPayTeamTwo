from src import credentials
from src import url
from src.PageObjects.page import Page


class Login(Page):

    def __init__(self, driver, base_url=url.login_page):
        super().__init__(driver)
        driver.get(base_url)

    def set_email(self, email):
        self.driver.find_element_by_id('email').clear()
        self.driver.find_element_by_id('email').send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)

    def sign_in(self):
        self.driver.find_element_by_id('Login_button').click()

    def login_as_admin(self):
        self.set_email(credentials.admin_email)
        self.set_password(credentials.admin_password)
        self.sign_in()

    def login_as_manager(self):
        self.set_email(credentials.manager_email)
        self.set_password(credentials.manager_password)
        self.sign_in()

    def login_as_inspector(self):
        self.set_email(credentials.inspector_email)
        self.set_password(credentials.inspector_password)
        self.sign_in()

    def login_as_user(self):
        self.set_email(credentials.user_email)
        self.set_password(credentials.user_password)
        self.sign_in()


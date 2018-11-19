from src import credentials
from src.PageObjects.page import Page
from src.Utilities.logger import logger
from src.locators import HomePage


class Login(Page):

    log = logger()

    def __init__(self, driver, base_url=''):
        super().__init__(driver, base_url)

    def set_email(self, email):
        self.get_element('email', 'id').clear()
        self.send_keys_to_element(email, 'email', 'id')

    def set_password(self, password):
        self.get_element('password', 'id').clear()
        self.send_keys_to_element(password, 'password', 'id')

    def sign_in(self):
        self.click_on_element('Login_button', 'id')

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.sign_in()
        self.wait_for_element(HomePage.display_name)

    def login_as_admin(self):
        self.login(credentials.admin_email, credentials.admin_password)
        return self

    def login_as_manager(self):
        self.login(credentials.manager_email, credentials.manager_password)
        return self

    def login_as_inspector(self):
        self.login(credentials.inspector_email, credentials.inspector_password)
        return self

    def login_as_user(self):
        self.login(credentials.user_email, credentials.user_password)
        return self

from src import params
from src.Page import Page


class Login(Page):

    def __init__(self, driver, baseUrl='http://localhost:8080/loginPage'):
        super().__init__(driver)
        driver.get(baseUrl)

    def set_email(self, email):
        self.driver.find_element_by_id('email').clear()
        self.driver.find_element_by_id('email').send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id('password').clear()
        self.driver.find_element_by_id('password').send_keys(password)

    def sign_in(self):
        self.driver.find_element_by_id('Login_button').click()

    def login_as_admin(self):
        self.set_email(params.admin_email)
        self.set_password(params.admin_password)
        self.sign_in()

    def login_as_manager(self):
        self.set_email(params.manager_email)
        self.set_password(params.manager_password)
        self.sign_in()

    def login_as_inspector(self):
        self.set_email(params.inspector_email)
        self.set_password(params.inspector_password)
        self.sign_in()

    def login_as_user(self):
        self.set_email(params.user_email)
        self.set_password(params.user_password)
        self.sign_in()


from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep


class LoginPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")

    def open_login_page(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(1)

    def input_email(self):
        self.input('*****', *self.EMAIL_FIELD)

    def input_password(self):
        self.input('*****', *self.PASSWORD_FIELD)

    def click_continue_btn(self):
        self.wait_for_element_click(*self.LOGIN_BTN)

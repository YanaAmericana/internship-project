from pages.base_page import Page
from pages.change_password_page import ChangePasswordPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)

        self.change_password_page = ChangePasswordPage(driver)
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)

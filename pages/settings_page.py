from selenium.webdriver.common.by import By

from pages.base_page import Page


class SettingsPage(Page):
    CHANGE_PASSWORD_BTN = (By.CSS_SELECTOR, "[href='/set-new-password']")

    def click_change_password(self):
        self.click(*self.CHANGE_PASSWORD_BTN)

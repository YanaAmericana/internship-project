from selenium.webdriver.common.by import By

from pages.base_page import Page


class HomePage(Page):
    SETTINGS_OPTION_BTN = (By.CSS_SELECTOR, "[href='/settings'] [class='menu-button-text']")

    def click_settings(self):
        self.click(*self.SETTINGS_OPTION_BTN)

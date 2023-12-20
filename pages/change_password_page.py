from selenium.webdriver.common.by import By

from pages.base_page import Page


class ChangePasswordPage(Page):
    CHANGE_PW_BTN = (By.CSS_SELECTOR, "[wized='changePasswordButton']")
    NEW_PW_FIELD = (By.ID, 'Enter-new-password')
    REENTER_NEW_PW_FIELD = (By.ID, 'Repeat-password')

    def verify_correct_page_loaded(self, url):
        self.verify_url(url)

    def enter_new_pw(self):
        self.input("12345", *self.NEW_PW_FIELD)

    def re_enter_new_pw(self):
        self.input("12345", *self.REENTER_NEW_PW_FIELD)

    def verify_change_pw_btn_available(self):
        self.wait_for_element_click(*self.CHANGE_PW_BTN)

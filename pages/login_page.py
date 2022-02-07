from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_email_area()
        self.should_be_password_area()
        self.should_be_submit_button()

    def should_be_email_area(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_AREA), 'No Email area'

    def should_be_password_area(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_AREA), 'No password area'

    def should_be_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_LOGIN_BTN), 'No button'


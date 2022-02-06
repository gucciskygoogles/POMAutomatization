from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators

class MainPage(BasePage):

    def should_be_login_btn(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_BTN), 'No login button'
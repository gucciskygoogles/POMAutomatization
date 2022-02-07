from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

class MainPage(BasePage):

    def should_be_login_btn(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_BTN), 'No login button'

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_BTN)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
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

    def open_side_bar(self):
        side_bar = self.browser.find_element(*MainPageLocators.SIDE_BAR_OPENER)
        side_bar.click()
        assert self.is_element_present(*MainPageLocators.SIDE_BAR_QUESTIONS), "We don't have side bar button"

    def click_on_logo(self):
        logo = self.browser.find_element(*MainPageLocators.STACKOVERFLOW_LOGO)
        logo.click()
        assert self.browser.current_url == 'https://stackoverflow.com/', "This url doesn't below to main page"
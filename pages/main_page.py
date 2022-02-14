import time

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.questions_page import QuestionsPage
from pages.about_page import AboutPage

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
        time.sleep(2)
        assert self.is_element_present(*MainPageLocators.SIDE_BAR_QUESTIONS), "We don't have side bar button"

    def click_on_logo(self):
        logo = self.browser.find_element(*MainPageLocators.STACKOVERFLOW_LOGO)
        logo.click()
        time.sleep(3)
        try:
            self.alert_remove()
        except:
            print('no alert')
        assert self.browser.current_url == 'https://stackoverflow.com/', "This url doesn't below to main page"

    def going_to_side_bar_questions(self):
        self.open_side_bar()
        question_chapter = self.browser.find_element(*MainPageLocators.SIDE_BAR_QUESTIONS)
        question_chapter.click()
        return QuestionsPage(browser=self.browser, url=self.browser.current_url)

    def going_to_about_page(self):
        about_page = self.browser.find_element(*MainPageLocators.ABOUT_BTN)
        about_page.click()
        return AboutPage(browser=self.browser, url=self.browser.current_url)

from pages.base_page import BasePage
from pages.locators import AboutPageLocators


class AboutPage(BasePage):

    def should_be_about_page(self):
        self.should_be_take_a_tour_btn()
        self.should_be_about_page_url()

    def should_be_take_a_tour_btn(self):
        assert self.is_element_present(*AboutPageLocators.TAKE_A_TOUR_BTN)

    def should_be_about_page_url(self):
        assert self.browser.current_url == 'https://stackoverflow.co/', 'This is not about page'
from pages.base_page import BasePage
from pages.locators import QuestionsPageLocators


class QuestionsPage(BasePage):

    def should_be_questions_page(self):
        self.should_be_ask_question_button()
        self.should_be_questions_url()

    def should_be_ask_question_button(self):
        assert self.is_element_present(*QuestionsPageLocators.ASK_QUESTION_BTN)

    def should_be_questions_url(self):
        assert self.browser.current_url == 'https://stackoverflow.com/questions', "Doesn't questions page url"
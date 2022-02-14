from pages.main_page import MainPage
import time

class TestSideBarMenu:

    def test_open_side_bar(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.open_side_bar()

    '''
    Need to understand some issues in this test
    
    def test_going_to_questions_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.open_side_bar()
        time.sleep(3)
        question_page = page.going_to_side_bar_questions()
        question_page.should_be_questions_page()
    '''

class TestWorkOnMainPage:

    def test_login_btn_is_here(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_btn()
        time.sleep(3)

    def test_logo_link_is_going_to_main_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.click_on_logo()


class TestFromMainPAgeToOther:

    def test_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

    def test_going_to_about_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        about_page = page.going_to_about_page()
        about_page.should_be_about_page_url()
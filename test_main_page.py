from pages.main_page import MainPage
import time

class TestWorkOnMainPage():

    def test_login_btn_is_here(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_btn()
        time.sleep(3)

    def test_logo_link_is_going_to_main_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.click_on_logo()

    def test_open_side_bar(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.open_side_bar()


class TestFromMainPAgeToOther:

    def test_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()
        login_page.should_be_google_login_button()
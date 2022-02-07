from pages.main_page import MainPage
import time


def test_login_btn_is_here(browser):
    link = 'https://stackoverflow.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_btn()
    time.sleep(3)

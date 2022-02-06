import pytest
from pages.main_page import MainPage
import time


def test_login_btn_is_here(browser):
    link = 'https://stackoverflow.com/'
    page = MainPage(browser, link)
    page.open()
    page.shoul_be_login_btn()

def test_go_to_login(browser):
    link = 'https://stackoverflow.com/'
    page = MainPage(browser, link)
    page.open()
    page.to_login_page()
    time.sleep(3)
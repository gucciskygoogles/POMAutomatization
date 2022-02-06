from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def to_login_page(self):
        login_btn = self.browser.find_element(By.XPATH, '/html/body/header/div/ol[2]/li[2]/a[1]')
        login_btn.click()

    def shoul_be_login_btn(self):
        self.browser.find_element(By.XPATH, '/html/body/header/div/ol[2]/li[2]/a[1]')
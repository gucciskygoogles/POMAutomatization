from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_BTN = (By.XPATH, '/html/body/header/div/ol[2]/li[2]/a[1]')

class LoginPageLocators():
    EMAIL_AREA = (By.ID, 'email')
    PASSWORD_AREA = (By.ID, 'password')
    SUBMIT_LOGIN_BTN = (By.ID, 'submit-button')
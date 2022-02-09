from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_BTN = (By.XPATH, '/html/body/header/div/ol[2]/li[2]/a[1]')
    SIDE_BAR_OPENER = (By.CLASS_NAME, 'left-sidebar-toggle')
    SIDE_BAR_QUESTIONS = (By.LINK_TEXT, 'Questions')
    STACKOVERFLOW_LOGO = (By.CLASS_NAME, '-logo')

class LoginPageLocators():
    EMAIL_AREA = (By.ID, 'email')
    PASSWORD_AREA = (By.ID, 'password')
    SUBMIT_LOGIN_BTN = (By.ID, 'submit-button')
    GOOGLE_LOGIN_BTN = (By.CLASS_NAME, 's-btn__google')
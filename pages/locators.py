from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BTN = (By.XPATH, '/html/body/header/div/ol[2]/li[2]/a[1]')
    SIDE_BAR_OPENER = (By.CLASS_NAME, 'left-sidebar-toggle')
    SIDE_BAR_QUESTIONS = (By.XPATH, '//*[@id="nav-questions"]/span')
    ABOUT_BTN = (By.XPATH, '/html/body/header/div/ol[1]/li[1]')
    STACKOVERFLOW_LOGO = (By.CLASS_NAME, '-logo')


class LoginPageLocators:
    EMAIL_AREA = (By.ID, 'email')
    PASSWORD_AREA = (By.ID, 'password')
    SUBMIT_LOGIN_BTN = (By.ID, 'submit-button')
    GOOGLE_LOGIN_BTN = (By.CLASS_NAME, 's-btn__google')

class QuestionsPageLocators:
    ASK_QUESTION_BTN = (By.LINK_TEXT, 'Ask Question')

class AboutPageLocators:
    TAKE_A_TOUR_BTN = (By.LINK_TEXT, 'Take a tour')
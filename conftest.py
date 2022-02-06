import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help='Выберите браузер, Chrome или Firefox')
    parser.addoption('--language', action='store', default=None,
                     help='Выберите язык, en или ru')

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome' or browser_name == 'Chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'user_language'})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox' or browser_name == 'Firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", 'user_languages')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name доллжен быть Firefox или Chrome')
    yield browser
    browser.quit()
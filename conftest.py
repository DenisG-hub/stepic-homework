from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default='ru',
                     help="Choose lang: es or ru")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("lang")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    # sleep(5)
    print("\nquit browser..")
    browser.quit()

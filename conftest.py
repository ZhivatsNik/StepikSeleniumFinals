import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# функция определяет необходимость вводить параметр language в командной строке при запуске теста
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language: en, es, fr")

# функция определяет браузер какой локализации запускать
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()




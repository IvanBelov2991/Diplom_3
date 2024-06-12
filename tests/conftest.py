import pytest
from selenium import webdriver
import data


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.maximize_window()
    browser.get(data.Urls.MAIN_PAGE)

    yield browser

    browser.quit()
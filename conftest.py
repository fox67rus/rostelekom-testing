import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from ctypes import windll

from pages.auth_page import AuthPage


@pytest.fixture(scope="session")
def browser():
    s = Service(r"\webdrivers\chromedriver.exe")
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="module")
def go_to_register_page(browser):
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_link_registration()
    assert 'registration' in browser.current_url


@pytest.fixture(scope="session")
def clear_clipboard():
    """Очистка буфера обмена"""
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['ru_RU']


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return 12345


@pytest.fixture()
def faker_locale():
    return ['ja_JP', 'en_US']

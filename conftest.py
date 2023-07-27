import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from ctypes import windll


@pytest.fixture(scope="session")
def browser():
    s = Service(r"\webdrivers\chromedriver.exe")
    chrome_options = Options()
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def clear_clipboard():
    """Очистка буфера обмена"""
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

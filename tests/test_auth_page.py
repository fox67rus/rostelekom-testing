from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config import *
from pages.auth_page import AuthPage


@pytest.mark.skip(reason="no way of currently testing this")
def test_open_auth_page(browser):
    """
    Проверка корректного открытия формы авторизации
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.find_element((By.CSS_SELECTOR, ".card-container__title")).text == "Авторизация"
    sleep(10)  # для контроля


def test_login_with_email(browser):
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.enter_login(VALID_EMAIL)
    auth.enter_password(VALID_PASSWORD)
    sleep(5)
    auth.click_to_login_button_()
    sleep(10)

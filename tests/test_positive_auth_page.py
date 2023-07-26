from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config import *
from pages.auth_page import AuthPage


def test_open_auth_page(browser):
    """
    Проверка корректного открытия формы авторизации
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.find_element((By.CSS_SELECTOR, ".card-container__title")).text == "Авторизация"
    sleep(5)  # для контроля


def test_active_tab_is_phone(browser):
    """
    Проверка выбора по умолчанию формы авторизации по телефону
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.active_tab_text() == "Телефон"


@pytest.mark.skip(reason="there is currently no need to test this")
def test_login_with_email(browser):
    """
    Проверка авторизации существующего пользователя по электронной почте с помощью кнопки Войти
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.enter_login(VALID_EMAIL)
    auth.enter_password(VALID_PASSWORD)
    sleep(5)
    auth.click_to_login_button()
    assert 'account_b2c' in browser.current_url
    browser.save_screenshot('result.png')
    sleep(5)  # для контроля


from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config import *
from pages.auth_page import AuthPage


# 15
@pytest.mark.current
def test_login_with_invalid_email(browser):
    """
    Проверка авторизации несуществующего пользователя по электронной почте с помощью кнопки Войти
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    sleep(0.5)
    auth.enter_login(INVALID_EMAIL)
    sleep(0.5)
    auth.enter_password(INVALID_PASSWORD)
    # sleep(10)  # ввод капчи
    # снять галочку Запомнить меня
    auth.click_to_checkbox_remember_me()
    auth.click_to_login_button()

    assert auth.get_error_message_text() == 'Неверный логин или пароль'


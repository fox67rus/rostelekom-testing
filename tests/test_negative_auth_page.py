from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config import *
from pages.auth_page import AuthPage


# 16
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

    assert auth.get_form_error_message_text() == 'Неверный логин или пароль'


# 17
@pytest.mark.current
def test_login_with_empty_data(browser):
    """
    Проверка авторизации с пустым именем пользователя и паролем
    """
    auth = AuthPage(browser)

    # словарь с методами перехода по табу, название таба и сообщение об ошибки при незаполненном имени пользователя
    tabs_data = {
        'email': [auth.click_to_tab_email, 'Почта', 'Введите адрес, указанный при регистрации'],
        'phone': [auth.click_to_tab_phone, 'Телефон', 'Введите номер телефона'],
        'login': [auth.click_to_tab_login, 'Логин', 'Введите логин, указанный при регистрации'],
        'ls': [auth.click_to_tab_ls, 'Лицевой счёт', 'Введите номер вашего лицевого счета']
    }

    auth.go_to_site()
    sleep(0.5)
    for tab in tabs_data.keys():
        tabs_data[tab][0]()
        assert auth.get_active_tab_text() == tabs_data[tab][1]
        auth.enter_login('')
        sleep(0.5)
        auth.enter_password('')
        # снять галочку Запомнить меня
        auth.click_to_checkbox_remember_me()
        auth.click_to_login_button()

        assert auth.get_error_message_text() == tabs_data[tab][2]
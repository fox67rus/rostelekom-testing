from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config import *
from pages.auth_page import AuthPage


# 1
# @pytest.mark.skip(reason="there is currently no need to test this")
def test_open_auth_page(browser):
    """
    Проверка корректного открытия формы авторизации
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.find_element((By.CSS_SELECTOR, ".card-container__title")).text == "Авторизация"
    # sleep(5)  # для контроля


# 2
# @pytest.mark.skip(reason="there is currently no need to test this")
def test_active_tab_is_phone(browser):
    """
    Проверка выбора по умолчанию таба авторизации по телефону
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.get_active_tab_text() == "Телефон"


# 3
# @pytest.mark.skip(reason="there is currently no need to test this")
def test_login_with_email_on_button_click(browser):
    """
    Проверка авторизации существующего пользователя по электронной почте с помощью кнопки Войти
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.enter_login(VALID_EMAIL)
    auth.enter_password(VALID_PASSWORD)
    auth.click_to_login_button()
    assert 'account_b2c' in browser.current_url
    browser.save_screenshot('result.png')
    # sleep(5)  # для контроля


# 4
# @pytest.mark.skip(reason="there is currently no need to test this")
def test_auto_change_tab_email(browser):
    """
    Проверка, что при вводе электронного адреса таб выбора аутентификации меняется на Почта
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.enter_login(VALID_EMAIL)
    auth.enter_password(VALID_PASSWORD)
    assert auth.get_active_tab_text() == "Почта"
    # sleep(3)  # для контроля


# 5
# @pytest.mark.skip(reason="there is currently no need to test this")
def test_auto_change_tab_login(browser):
    """
    Проверка, что при вводе логина таб выбора аутентификации меняется на Логин
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.enter_login(VALID_LOGIN)
    auth.enter_password(VALID_PASSWORD)
    assert auth.get_active_tab_text() == "Логин"
    # sleep(3)  # для контроля


# 6
# @pytest.mark.skip(reason="there is currently no need to test this")
def test_auto_change_tab_ls(browser):
    """
    Проверка, что при вводе лицевого счёта таб выбора аутентификации меняется на Лицевой счёт
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    # Выбираем таб Почта
    auth.click_to_tab_email()
    auth.enter_login(VALID_LS)
    auth.enter_password(VALID_PASSWORD)
    assert auth.get_active_tab_text() == "Лицевой счёт"
    # sleep(3)  # для контроля


# 7
# @pytest.mark.skip(reason="there is currently no need to test this")
@pytest.mark.current
def test_auto_change_tab_phone_from_login(browser):
    """
    Проверка, что при вводе мобильного телефона на вкладке Логин таб выбора аутентификации автоматически меняется на Номер
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    # переключаем таб на логин
    auth.click_to_tab_login()
    assert auth.get_active_tab_text() == "Логин"
    # очищаем поля
    auth.clear_login()
    auth.clear_password()
    assert auth.get_login_value() == "", 'Поля не очищены'

    auth.enter_login(VALID_PHONE)
    auth.enter_password(VALID_PASSWORD)
    # sleep(3)  # для контроля
    assert auth.get_active_tab_text() == "Телефон"

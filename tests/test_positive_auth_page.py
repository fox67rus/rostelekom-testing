from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config import *
from pages.auth_page import AuthPage
from pages.user_page import UserPage

pytestmark = [pytest.mark.positive, pytest.mark.auth]  # маркировка всех тестов модуля


def test_open_auth_page(browser):
    """
    Проверка корректного открытия формы авторизации
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.find_element((By.CSS_SELECTOR, ".card-container__title")).text == "Авторизация"
    # sleep(5)  # для контроля


@pytest.mark.skip(reason="no way of currently testing this")
def test_active_tab_is_phone(browser):
    """
    Проверка, что по умолчанию выбран таб авторизации по телефону
    """
    sleep(5)
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.get_active_tab_text() == "Телефон"


@pytest.mark.smoke
def test_login_with_email_on_button_click(browser):
    """
    Проверка авторизации существующего пользователя по электронной почте с помощью кнопки Войти
    """
    auth = AuthPage(browser)
    user_page = UserPage(browser)
    auth.go_to_site()
    sleep(0.5)
    auth.enter_login(VALID_EMAIL)
    sleep(0.5)
    auth.enter_password(VALID_PASSWORD)
    sleep(0.5)
    # снять галочку Запомнить меня
    auth.click_to_checkbox_remember_me()
    auth.click_to_login_button()
    assert 'account_b2c' in browser.current_url
    browser.save_screenshot('result.png')
    # выход из личного кабинета
    user_page.click_logout()
    sleep(5)  # для контроля


def test_auto_change_tab_email_from_phone(browser):
    """
    Проверка, что при вводе электронного адреса в поле Телефон таб выбора аутентификации меняется на Почта
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_tab_phone()
    auth.enter_login(VALID_EMAIL)
    auth.enter_password(VALID_PASSWORD)
    assert auth.get_active_tab_text() == "Почта"
    # sleep(3)  # для контроля


def test_auto_change_tab_email_from_login(browser):
    """
    Проверка, что при вводе электронного адреса в поле Логин таб выбора аутентификации меняется на Почта
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_tab_login()
    auth.enter_login(VALID_EMAIL)
    auth.enter_password(VALID_PASSWORD)
    assert auth.get_active_tab_text() == "Почта"
    # sleep(3)  # для контроля


def test_auto_change_tab_login_from_phone(browser):
    """
    Проверка, что при вводе логина в поле Телефон таб выбора аутентификации меняется на Логин
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_tab_phone()
    auth.enter_login(VALID_LOGIN)
    auth.enter_password(VALID_PASSWORD)
    assert auth.get_active_tab_text() == "Логин"
    # sleep(3)  # для контроля


def test_auto_change_tab_ls_from_email(browser):
    """
    Проверка, что при вводе лицевого счёта в поле Почта таб выбора аутентификации меняется на Лицевой счёт
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    # Выбираем таб Почта
    auth.click_to_tab_email()
    auth.enter_login(VALID_LS)
    auth.enter_password(VALID_PASSWORD)
    assert auth.get_active_tab_text() == "Лицевой счёт"
    # sleep(3)  # для контроля


def test_auto_change_tab_phone_from_login(browser):
    """
    Проверка, что при вводе номера телефона на вкладке Логин таб выбора аутентификации автоматически меняется на Номер
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    # переключаем таб на логин
    auth.click_to_tab_login()
    assert auth.get_active_tab_text() == "Логин"
    # очищаем поля
    auth.clear_login()
    auth.clear_password()
    assert auth.get_login_value() == "", 'Поля формы не очищены'

    auth.enter_login(VALID_PHONE)
    auth.enter_password(VALID_PASSWORD)
    # sleep(3)  # для контроля
    assert auth.get_active_tab_text() == "Телефон"


def test_open_user_agreement_on_link(browser):
    """
    Проверка, что при нажатии на ссылку открывается пользовательское соглашение
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    # сохраняем ID оригинального окна
    original_window = browser.current_window_handle
    assert len(browser.window_handles) == 1, 'открыты лишние вкладки'
    # нажимаем ссылку с соглашением
    auth.click_to_agreement_link()

    # в открытых вкладках ищем отличную от первой
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break
    assert browser.title == 'User agreement'
    # sleep(3)  # для контроля


def test_open_vk_auth_on_click(browser):
    """
    При нажатии на кнопку авторизации через Вконтакте осуществляется переход на страницу соцсети
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_ico_vk()
    assert 'id.vk.com' in browser.current_url
    # sleep(3)  # для контроля


def test_open_ok_auth_on_click(browser):
    """
    При нажатии на кнопку авторизации через Одноклассники осуществляется переход на страницу соцсети
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_ico_ok()
    assert 'connect.ok.ru' in browser.current_url
    # sleep(3)  # для контроля


def test_open_mail_auth_on_click(browser):
    """
    При нажатии на кнопку авторизации через Mail осуществляется переход на страницу соцсети
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_ico_mail()
    assert 'connect.mail.ru' in browser.current_url
    # sleep(3)  # для контроля


def test_open_yandex_auth_on_click(browser):
    """
    При нажатии на кнопку авторизации через Яндекс осуществляется переход на страницу соцсети
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_ico_ya()
    assert 'passport.yandex.ru' in browser.current_url


@pytest.mark.smoke
def test_open_page_reset_password_on_link_click(browser):
    """
    Проверка корректного открытия страницы Восстановления пароля при нажатии на ссылку
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_link_forgot_password()
    assert 'login-actions/reset-credentials' in browser.current_url


@pytest.mark.smoke
def test_open_page_registration_on_link_click(browser):
    """
    Проверка корректного открытия страницы Регистрации при нажатии на ссылку
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_link_registration()
    assert 'registration' in browser.current_url


def test_support_phone_contains_correct_link(browser):
    """
    Проверка корректности указанной ссылки для звонка в службу поддержки
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.get_support_phone_href() == 'tel:' + auth.base_phone

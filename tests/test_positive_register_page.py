from time import sleep

import pytest

from pages.auth_page import AuthPage
from pages.register_page import RegisterPage
from testdata import generate_russian_string

pytestmark = [pytest.mark.positive, pytest.mark.register]  # маркировка всех тестов модуля


def test_register_with_correct_data(browser, faker):
    """
    Проверка, что при нажатии на кнопку Зарегистрироваться с заполненными корректными данными происходит отправка кода
    подтверждения
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_link_registration()
    assert 'registration' in browser.current_url
    register = RegisterPage(browser)
    sleep(0.5)
    # register.enter_first_name('Михаил')
    register.enter_first_name(faker.first_name())
    sleep(0.5)
    # register.enter_last_name('Булгаков')
    register.enter_last_name(faker.last_name())
    sleep(0.5)
    register.enter_user_name('xaset20266@naymedia.com')
    sleep(0.5)
    register.enter_password('1234-Qwerty')
    sleep(0.5)
    register.enter_password_confirm('1234-Qwerty')
    sleep(0.5)
    register.click_to_register_button()

    assert register.get_header_h1_text() == 'Подтверждение email'
    # sleep(3)  # для контроля


@pytest.mark.current
@pytest.mark.parametrize(
    "first_name_value",
    [
        "Иван",
        "Ян",
        "Лия",
        generate_russian_string(29),
        generate_russian_string(30),
        "Анна-Мария",
        "МИХАИЛ",
        "капитолина"
    ],
    ids=[
        "Common",
        "2 symbols",
        "3 symbols",
        "29 symbols",
        "30 symbols",
        "dash",
        "UPPER",
        "lower"]
)
def test_field_first_name(browser, first_name_value, go_to_register_page):
    """
    Проверка, что при вводе допустимых значений в поле Имя не возникает сообщения об ошибке.
    Проверка граничных значений
    """
    register = RegisterPage(browser)
    assert register.get_header_h1_text() == 'Регистрация', "Открыта не страница регистрации"
    sleep(0.5)  # антикапча
    register.enter_first_name(first_name_value)
    sleep(0.5)  # антикапча
    register.click_to_register_button()

    # sleep(3)  # для контроля
    assert len(
        register.get_meta_error_message()) == 4, 'Появилось сообщение об ошибке'
    register.clear_registration_form()  # очистка полей формы


@pytest.mark.parametrize(
    "last_name_value",
    ["Иванов", "Ли", "Ким", generate_russian_string(29), generate_russian_string(30), "Мамин-Сибиряк"],
    ids=["Common", "2 symbols", "3 symbols", "29 symbols", "30 symbols", "dash"]
)
def test_field_last_name(browser, last_name_value, go_to_register_page):
    """
    Проверка, что при вводе допустимых значений в поле Фамилия не возникает сообщения об ошибке.
    Проверка граничных значений
    """
    register = RegisterPage(browser)
    assert register.get_header_h1_text() == 'Регистрация', "Открыта не страница регистрации"
    register.clear_registration_form()  # очистка полей формы
    sleep(0.5)  # антикапча
    register.enter_last_name(last_name_value)
    sleep(0.5)  # антикапча
    register.click_to_register_button()

    # sleep(3)  # для контроля
    assert len(
        register.get_meta_error_message()) == 4, 'Появилось сообщение об ошибке'


@pytest.mark.parametrize(
    "password_value",
    [
        "123456Ab",
        "1234567Ab",
        "123456789QwertyAsdf",
        "123456789QwertyAsdfg",
        "`~@#$%^&*()_+|{-=Ab"
    ],
    ids=[
        "8 symbols (digit + upper + lower)",
        "9 symbols (digit + upper + lower)",
        "19 symbols (digit + upper + lower)",
        "20 symbols (digit + upper + lower)",
        "19 symbols (special + upper + lower)"
    ]
)
def test_field_password_correct_data(browser, password_value: str, go_to_register_page):
    """
    Проверка, что при вводе недопустимых значений в поле Пароль возникает сообщение об ошибке
    """
    register = RegisterPage(browser)
    assert register.get_header_h1_text() == 'Регистрация', "Открыта не страница регистрации"
    sleep(0.5)  # антикапча
    register.enter_password(password_value)
    sleep(0.5)  # антикапча
    register.click_to_register_button()
    assert register.get_meta_error_message()[0], 'Отсутствует сообщение об ошибке'

    # sleep(3)  # для контроля
    register.clear_registration_form()  # очистка полей формы

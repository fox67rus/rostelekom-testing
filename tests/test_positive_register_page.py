from time import sleep

import pytest

from pages.register_page import RegisterPage
from testdata import generate_russian_string


@pytest.mark.register
def test_register_with_correct_data(browser, go_to_register_page, faker):
    """
    Проверка, что при нажатии на кнопку Зарегистрироваться с заполненными корректными данными происходит отправка кода подтверждения
    """
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
    sleep(0.5)

    assert register.get_header_h1_text() == 'Подтверждение email'
    # sleep(3)  # для контроля


@pytest.mark.register
@pytest.mark.parametrize(
    "first_name_value",
    ["Иван", "Ян", "Лия", generate_russian_string(29), generate_russian_string(30)],
    ids=["Common", "2 symbols", "3 symbols", "29 symbols", "30 symbols"]
)
def test_field_first_name(browser, first_name_value, go_to_register_page):
    """
    Проверка, что при вводе допустимых значений в поле Имя не возникает сообщения об ошибке.
    Проверка граничных значений
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_first_name(first_name_value)
    sleep(0.5)  # антикапча
    register.click_to_register_button()

    # sleep(3)  # для контроля
    assert len(
        register.get_meta_error_message()) == 4, 'Появилось сообщение об ошибке'
    register.clear_registration_form()  # очистка полей формы


@pytest.mark.current
@pytest.mark.register
@pytest.mark.parametrize(
    "last_name_value",
    ["Иванов", "Ли", "Лия", generate_russian_string(29), generate_russian_string(30), "Анна-Мария", "И ван"],
    ids=["Common", "2 symbols", "3 symbols", "29 symbols", "30 symbols", "dash", "space"]
)
def test_field_last_name(browser, last_name_value, go_to_register_page):
    """
    Проверка, что при вводе допустимых значений в поле Фамилия не возникает сообщения об ошибке.
    Проверка граничных значений
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_last_name(last_name_value)
    sleep(0.5)  # антикапча
    register.click_to_register_button()

    # sleep(3)  # для контроля
    assert len(
        register.get_meta_error_message()) == 4, 'Появилось сообщение об ошибке'
    register.clear_registration_form()  # очистка полей формы

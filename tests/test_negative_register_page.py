from time import sleep

import pytest

from pages.register_page import RegisterPage


@pytest.mark.current
@pytest.mark.register
def test_register_with_empty_data(browser, go_to_register_page):
    """
    Проверка регистрации с незаполненными полями
    """
    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_first_name('')
    sleep(0.5)  # антикапча
    register.enter_last_name('')
    sleep(0.5)  # антикапча
    register.enter_user_name('')
    sleep(0.5)  # антикапча
    register.enter_password('')
    sleep(0.5)  # антикапча
    register.enter_password_confirm('')
    sleep(0.5)  # антикапча
    register.click_to_register_button()
    sleep(0.5)  # антикапча

    assert register.get_header_h1_text() == 'Регистрация'
    assert len(register.get_meta_error_message()) == 5, 'Количество сообщений об ошибках не соответствует количеству полей'
    # sleep(5)  # для контроля


@pytest.mark.current
@pytest.mark.register
@pytest.mark.parametrize(
    "first_name_value",
    ["", "А", "Оченьоченьдлинноеимядлятеставот", "Michael", "袁世凱", "12345"],
    ids=["empty", "1 symbol", "31 symbol", "in English", "china", "digit"]
)
def test_field_first_name(browser, first_name_value, go_to_register_page):
    """
    Проверка, что при вводе недопустимых значений в поле Имя возникает сообщение об ошибке
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_first_name(first_name_value)
    sleep(0.5)  # антикапча
    register.enter_last_name("Фамилия")

    assert register.get_meta_error_message()[0] == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    sleep(3)  # для контроля

    assert register.get_header_h1_text() == 'Регистрация'

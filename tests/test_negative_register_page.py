from time import sleep

import pytest

from pages.register_page import RegisterPage
from testdata import special_chars, generate_string, generate_russian_string, chinese_chars

pytestmark = [pytest.mark.negative, pytest.mark.register]  # маркировка всех тестов модуля


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
    assert len(
        register.get_meta_error_message()) == 5, 'Количество сообщений об ошибках не соответствует количеству полей'
    register.clear_registration_form()  # очистка полей формы
    # sleep(5)  # для контроля


@pytest.mark.parametrize(
    "first_name_value",
    ["А", generate_russian_string(31), "Michael", chinese_chars(), "12345", special_chars(), "И ван"],
    ids=["1 symbol", "31 symbol", "in English", "china", "digit", "special_chars", "space"]
)
def test_field_first_name(browser, first_name_value, go_to_register_page):
    """
    Проверка, что при вводе недопустимых значений в поле Имя возникает сообщение об ошибке
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_first_name(first_name_value)
    # sleep(0.5)  # антикапча
    # register.enter_last_name("Фамилия")

    assert register.get_meta_error_message()[0], 'Отсутствует сообщение об ошибке'
    assert register.get_meta_error_message()[
               0] == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.', 'Не верное сообщение об ошибке'
    # sleep(3)  # для контроля

    assert register.get_header_h1_text() == 'Регистрация'
    register.clear_registration_form()  # очистка полей формы


@pytest.mark.parametrize(
    "last_name_value",
    ["А", generate_russian_string(31), "Jordan", chinese_chars(), "12345", special_chars(), "Мамин Сибиряк"],
    ids=["1 symbol", "31 symbol", "in English", "china", "digit", "special_chars", "space"]
)
def test_field_first_name(browser, last_name_value, go_to_register_page):
    """
    Проверка, что при вводе недопустимых значений в поле Фамилия возникает сообщение об ошибке
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_last_name(last_name_value)

    assert register.get_meta_error_message()[0], 'Отсутствует сообщение об ошибке'
    assert register.get_meta_error_message()[
               0] == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.', 'Не верное сообщение об ошибке'
    # sleep(3)  # для контроля

    assert register.get_header_h1_text() == 'Регистрация', 'Выполнен переход на другую страницу'
    register.clear_registration_form()  # очистка полей формы


@pytest.mark.parametrize(
    "user_name_value",
    ["example@email",
     generate_string(312) + "@email.ru",
     "exampleemail.ru",
     "exa mple@email.ru",
     "example@e mail.ru",
     "@email.ru",
     "example@",
     "имя@домен.рф",
     "Miles.O'Brian@example.com"
     ],
    ids=["email: no dot in domain",
         "email: 320+ symbols",
         "email: no @",
         "email: space in local",
         "email: space in domen",
         "email: empty local",
         "email: empty domen",
         "email: russian_chars",
         "apostrophe"
         ]
)
def test_field_user_name(browser, user_name_value, go_to_register_page):
    """
    Проверка, что при вводе недопустимых значений в поле E-mail или мобильный телефон возникает сообщение об ошибке
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_user_name(user_name_value)
    assert register.get_meta_error_message(), "Отсутствует сообщение об ошибке"
    assert register.get_meta_error_message()[
               0] == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru', \
        "Не верное сообщение об ошибке"
    # sleep(3)  # для контроля

    assert register.get_header_h1_text() == 'Регистрация'
    register.clear_registration_form()  # очистка полей формы


@pytest.mark.parametrize(
    "password_value",
    [
        "Abc",
        "12345Ab",
        generate_string(21),
        "01234567",
        "12345678A",
        "12345678a",
        "123Пароль",
        "Abcdefgh",
        special_chars()
    ],
    ids=[
        "3 symbols",
        "7 symbols",
        "21 symbols",
        "8 digit",
        "8 digit + upper",
        "8 digit + lower",
        "digit + russian",
        "only letters",
        "only special"
    ]
)
def test_field_password_incorrect_data(browser, password_value: str, go_to_register_page):
    """
    Проверка, что при вводе недопустимых значений в поле Пароль возникает сообщение об ошибке
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_password(password_value)

    uppers = [char for char in password_value if 65 <= ord(char) <= 90]  # заглавные буквы в пароле
    lowers = [char for char in password_value if 97 <= ord(char) <= 122]  # строчные буквы в пароле
    rus_letters = [char for char in password_value if char.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
    digit_and_spec = [char for char in password_value if char in '0123456789~`!@#$%^&*()_+?:"{}[];’']

    assert register.get_meta_error_message()[0], 'Отсутствует сообщение об ошибке'

    if len(password_value) < 8:
        assert register.get_meta_error_message()[0] == 'Длина пароля должна быть не менее 8 символов'
    elif len(password_value) > 20:
        assert register.get_meta_error_message()[0] == 'Длина пароля должна быть не более 20 символов'
    elif rus_letters:
        assert register.get_meta_error_message()[0] == 'Пароль должен содержать только латинские буквы'
    elif not uppers:
        assert register.get_meta_error_message()[0] == 'Пароль должен содержать хотя бы одну заглавную букву'
    elif uppers and not lowers:
        assert register.get_meta_error_message()[0] == 'Пароль должен содержать хотя бы одну строчную букву'
    elif not digit_and_spec:
        assert register.get_meta_error_message()[
                   0] == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

    print(f'{password_value=}, {register.get_meta_error_message()[0]}')  # для отладки
    # sleep(3)  # для контроля

    assert register.get_header_h1_text() == 'Регистрация'
    register.clear_registration_form()  # очистка полей формы

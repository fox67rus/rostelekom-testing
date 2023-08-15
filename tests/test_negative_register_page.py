from time import sleep

import pytest

from pages.register_page import RegisterPage
from testdata import special_chars, generate_string, generate_russian_string, chinese_chars, upper_in_str, lower_in_str, \
    rus_letters_in_str, digit_and_spec_in_str

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
     "Miles.O'Brian@example.com",
     "+7987654321",
     "+798765432100",
     "+375987654321",
     "+37598765432100"
     ],
    ids=["email: no dot in domain",
         "email: 320+ symbols",
         "email: no @",
         "email: space in local",
         "email: space in domain",
         "email: empty local",
         "email: empty domain",
         "email: russian_chars",
         "email: apostrophe",
         "phone Russia: without last digit",
         "phone Russia: 11 digit",
         "phone Belarus: without last digit",
         "phone Belarus: 11 digit"
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

    uppers = upper_in_str(password_value)  # заглавные буквы в пароле
    lowers = lower_in_str(password_value)  # строчные буквы в пароле
    rus_letters = rus_letters_in_str(password_value)  # русские символы в пароле
    digit_and_spec = digit_and_spec_in_str(password_value)  # цифры или спецсимволы в пароле

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

    # print(f'{password_value=}, {register.get_meta_error_message()[0]}')  # для отладки
    # sleep(3)  # для контроля

    assert register.get_header_h1_text() == 'Регистрация'
    register.clear_registration_form()  # очистка полей формы


@pytest.mark.parametrize(
    "password_value, password_confirm_value",
    [
        ("Abc", "Abc"),
        ("12345Ab", "12345Ab"),
        (generate_string(21), generate_string(21)),
        ("01234567", "01234567"),
        ("12345678A", "12345678A"),
        ("12345678a", "12345678a"),
        ("123Пароль", "123Пароль"),
        ("Abcdefgh", "Abcdefgh"),
        ("#$%^&*()-_=+`", "#$%^&*()-_=+`")
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
def test_field_password_confirm_incorrect_data(browser, password_value: str, password_confirm_value: str,
                                               go_to_register_page):
    """
    Проверка, что при вводе недопустимых значений в поле Подтверждение пароля возникает сообщение об ошибке
    """

    register = RegisterPage(browser)
    sleep(0.5)  # антикапча
    register.enter_password(password_value)
    sleep(0.5)  # антикапча
    register.enter_password_confirm(password_confirm_value)
    sleep(0.5)  # антикапча

    uppers = upper_in_str(password_confirm_value)  # заглавные буквы в пароле
    lowers = lower_in_str(password_confirm_value)  # строчные буквы в пароле
    rus_letters = rus_letters_in_str(password_confirm_value)  # русские символы в пароле
    digit_and_spec = digit_and_spec_in_str(password_confirm_value)  # цифры или спецсимволы в пароле

    assert register.get_meta_error_message()[1], 'Отсутствует сообщение об ошибке для поля Подтверждение пароля'

    if password_value != password_confirm_value:
        assert register.get_meta_error_message()[1] == 'Пароли не совпадают'
    elif len(password_confirm_value) < 8:
        assert register.get_meta_error_message()[1] == 'Длина пароля должна быть не менее 8 символов'
    elif len(password_confirm_value) > 20:
        assert register.get_meta_error_message()[1] == 'Длина пароля должна быть не более 20 символов'
    elif rus_letters:
        assert register.get_meta_error_message()[1] == 'Пароль должен содержать только латинские буквы'
    elif not uppers:
        assert register.get_meta_error_message()[1] == 'Пароль должен содержать хотя бы одну заглавную букву'
    elif uppers and not lowers:
        assert register.get_meta_error_message()[1] == 'Пароль должен содержать хотя бы одну строчную букву'
    elif not digit_and_spec:
        assert register.get_meta_error_message()[
                   1] == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

    print(f'{password_confirm_value=}, {register.get_meta_error_message()[1]}')  # для отладки
    # sleep(3)  # для контроля

    assert register.get_header_h1_text() == 'Регистрация'
    register.clear_registration_form()  # очистка полей формы


@pytest.mark.parametrize(
    "password_value, password_confirm_value",
    [
        ("123456Ab", "123456Ab"),
        ("1234567Ab", "1234567Ab"),
        ("123456789QwertyAsdf", "123456789QwertyAsdf"),
        ("123456789QwertyAsdfg", "123456789QwertyAsdfg"),
        ("`~@#$%^&*()_+|{-=Ab", "`~@#$%^&*()_+|{-=Ab"),
        ("Abc123deF", " Abc123deF"),
        ("Abc123deF", "Abc123deF ")
    ],
    ids=[
        "8 symbols (digit + upper + lower)",
        "9 symbols (digit + upper + lower)",
        "19 symbols (digit + upper + lower)",
        "20 symbols (digit + upper + lower)",
        "19 symbols (special + upper + lower)",
        "begin space",
        "end space"
    ]
)
def test_field_password_confirm_correct_data(browser, password_value: str, password_confirm_value: str,
                                             go_to_register_page):
    """
    Проверка, что при вводе допустимых значений в поле Подтверждение пароля не возникает сообщений об ошибке """
    register = RegisterPage(browser)
    assert register.get_header_h1_text() == 'Регистрация', "Открыта не страница регистрации"
    sleep(0.5)  # антикапча
    register.enter_password(password_value)
    sleep(0.5)  # антикапча
    register.enter_password_confirm(password_confirm_value)
    sleep(0.5)  # антикапча
    register.click_to_register_button()

    assert len(
        register.get_meta_error_message()) == 3, 'Появилось сообщение об ошибке'

    # sleep(3)  # для контроля
    register.clear_registration_form()  # очистка полей формы

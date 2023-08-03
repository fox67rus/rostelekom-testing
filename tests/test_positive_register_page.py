from time import sleep

import pytest

from pages.auth_page import AuthPage
from pages.register_page import RegisterPage


@pytest.mark.register
def test_register_with_correct_data(browser, go_to_register_page, faker):
    """
    Проверка регистрации с корректными данными
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
    sleep(5)  # для контроля

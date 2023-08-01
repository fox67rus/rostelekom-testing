from time import sleep

import pytest

from pages.auth_page import AuthPage
from pages.register_page import RegisterPage


# 18
@pytest.mark.register
def test_register_with_correct_data(browser):
    """
    Проверка регистрации с корректными данными
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_link_registration()
    assert 'registration' in browser.current_url

    register = RegisterPage(browser)
    sleep(0.5)
    register.enter_first_name('Михаил')
    sleep(0.5)
    register.enter_last_name('Булгаков')
    sleep(0.5)
    register.enter_user_name('xaset20266@naymedia.com')
    sleep(0.5)
    register.enter_password('1234-Qwerty')
    sleep(0.5)
    register.enter_password_confirm('1234-Qwerty')
    sleep(0.5)
    register.click_to_register_button()
    sleep(0.5)

    assert register.get_registration_confirm_text() == 'Подтверждение email'
    sleep(5)  # для контроля

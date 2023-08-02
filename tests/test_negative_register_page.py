from time import sleep

import pytest

from pages.auth_page import AuthPage
from pages.register_page import RegisterPage


# 19
@pytest.mark.register
def test_register_with_empty_data(browser):
    """
    Проверка регистрации с незаполненными полями
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.click_to_link_registration()
    assert 'registration' in browser.current_url

    register = RegisterPage(browser)
    sleep(0.5)
    register.enter_first_name('')
    sleep(0.5)
    register.enter_last_name('')
    sleep(0.5)
    register.enter_user_name('')
    sleep(0.5)
    register.enter_password('')
    sleep(0.5)
    register.enter_password_confirm('')
    sleep(0.5)
    register.click_to_register_button()
    sleep(0.5)

    assert register.get_header_h1_text() == 'Регистрация'
    sleep(5)  # для контроля

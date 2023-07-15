from time import sleep

import pytest
from selenium.webdriver.common.by import By

from config import *
from pages.auth_page import AuthPage


@pytest.mark.skip(reason="no way of currently testing this")
def test_open_auth_page(browser):
    """
    Проверка корректного открытия формы авторизации
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.find_element((By.CSS_SELECTOR, ".card-container__title")).text == "Авторизация"
    sleep(10)  # для контроля


def test_login_with_email(browser):
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.enter_login(VALID_EMAIL)
    auth.enter_password(VALID_PASSWORD)
    sleep(5)
    auth.click_to_login_button_()
    assert 'account_b2c' in browser.current_url
    browser.save_screenshot('result.png')
    # assert https://b2c.passport.rt.ru/account_b2c/page?state=e55b0a0e-2f69-4155-ae82-bea8bae6ce4c&client_id=account_b2c#/
    sleep(10)

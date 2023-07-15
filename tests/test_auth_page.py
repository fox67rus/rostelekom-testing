from time import sleep

from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage


def test_open_auth_page(browser):
    """
    Проверка корректного открытия формы авторизации
    """
    auth = AuthPage(browser)
    auth.go_to_site()
    assert auth.find_element((By.CSS_SELECTOR, ".card-container__title")).text == "Авторизация"
    sleep(10)


def test_login_with_email(browser):
    pass

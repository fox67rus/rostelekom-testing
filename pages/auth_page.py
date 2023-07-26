from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthPageLocators:
    LOCATOR_AUTH_PAGE_TAB_PHONE = (By.ID, 't-btn-tab-phone')
    LOCATOR_AUTH_PAGE_TAB_EMAIL = (By.ID, 't-btn-tab-mail')
    LOCATOR_AUTH_PAGE_TAB_LOGIN = (By.ID, 't-btn-tab-login')
    LOCATOR_AUTH_PAGE_TAB_LS = (By.ID, 't-btn-tab-ls')
    LOCATOR_AUTH_PAGE_ACTIVE_TAB = (By.CLASS_NAME, 'rt-tab--active')

    LOCATOR_AUTH_PAGE_FIELD_USERNAME = (By.ID, 'username')
    LOCATOR_AUTH_PAGE_FIELD_PASSWORD = (By.ID, 'password')
    LOCATOR_AUTH_PAGE_BUTTON_SUBMIT = (By.ID, 'kc-login')

    LOCATOR_AUTH_PAGE_CHECKBOX_REMEMBERME = (By.NAME, 'rememberMe')

    LOCATOR_AUTH_PAGE_BUTTON_FORGOTPASSWORD = (By.ID, 'forgot_password')


class AuthPage(BasePage):

    def enter_login(self, login_value):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_FIELD_USERNAME).send_keys(login_value)

    def enter_password(self, password_value):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_FIELD_PASSWORD).send_keys(password_value)

    def click_to_login_button(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_BUTTON_SUBMIT).click()

    def active_tab_text(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_ACTIVE_TAB).text

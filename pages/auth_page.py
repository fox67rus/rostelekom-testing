from selenium.webdriver import Keys
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

    LOCATOR_AUTH_PAGE_CHECKBOX_REMEMBER_ME = (By.CLASS_NAME, 'rt-checkbox__label')

    LOCATOR_AUTH_PAGE_BUTTON_FORGOT_PASSWORD = (By.ID, 'forgot_password')

    LOCATOR_AUTH_PAGE_LINK_AGREEMENT = (By.LINK_TEXT, 'пользовательского соглашения')

    LOCATOR_AUTH_PAGE_ICO_VK = (By.ID, 'oidc_vk')
    LOCATOR_AUTH_PAGE_ICO_OK = (By.ID, 'oidc_ok')
    LOCATOR_AUTH_PAGE_ICO_MAIL = (By.ID, 'oidc_mail')
    LOCATOR_AUTH_PAGE_ICO_YA = (By.ID, 'oidc_ya')


class AuthPage(BasePage):

    def enter_login(self, login_value):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_FIELD_USERNAME).send_keys(login_value)

    def enter_password(self, password_value):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_FIELD_PASSWORD).send_keys(password_value)

    def get_login_value(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_FIELD_USERNAME).get_attribute('value')

    def clear_login(self):
        login_field = self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_FIELD_USERNAME)
        login_field.send_keys(Keys.CONTROL + "a")
        login_field.send_keys(Keys.DELETE)

    def clear_password(self):
        password_field = self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_FIELD_PASSWORD)
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)

    def click_to_checkbox_remember_me(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_CHECKBOX_REMEMBER_ME).click()

    def click_to_login_button(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_BUTTON_SUBMIT).click()

    def get_active_tab_text(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_ACTIVE_TAB).text

    def click_to_tab_phone(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_TAB_PHONE).click()

    def click_to_tab_email(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_TAB_EMAIL).click()

    def click_to_tab_login(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_TAB_LOGIN).click()

    def click_to_tab_ls(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_TAB_LS).click()

    def click_to_agreement_link(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_LINK_AGREEMENT).click()

    def click_to_ico_vk(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_ICO_VK).click()

    def click_to_ico_ok(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_ICO_OK).click()

    def click_to_ico_mail(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_ICO_MAIL).click()

    def click_to_ico_ya(self):
        return self.find_element(AuthPageLocators.LOCATOR_AUTH_PAGE_ICO_YA).click()



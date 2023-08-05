from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPageLocators:
    LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME = (By.NAME, 'firstName')
    LOCATOR_REGISTER_PAGE_FIELD_LAST_NAME = (By.NAME, 'lastName')

    LOCATOR_REGISTER_PAGE_FIELD_USER_NAME = (By.ID, 'address')
    LOCATOR_REGISTER_PAGE_FIELD_PASSWORD = (By.ID, 'password')
    LOCATOR_REGISTER_PAGE_FIELD_PASSWORD_CONFIRM = (By.ID, 'password-confirm')

    LOCATOR_REGISTER_PAGE_BUTTON_REGISTER = (By.NAME, 'register')

    LOCATOR_REGISTER_PAGE_H1 = (By.TAG_NAME, 'h1')

    LOCATOR_REGISTER_PAGE_META_ERROR = (By.CLASS_NAME, 'rt-input-container__meta--error')


class RegisterPage(BasePage):
    def enter_first_name(self, first_name_value):
        locator_text_input = RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME
        self.enter_text_to_field(locator_text_input, first_name_value)

    def enter_last_name(self, last_name_value):
        locator_text_input = RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_LAST_NAME
        self.enter_text_to_field(locator_text_input, last_name_value)

    def enter_user_name(self, user_name_value):
        locator_text_input = RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_USER_NAME
        self.enter_text_to_field(locator_text_input, user_name_value)

    def enter_password(self, password_value):
        locator_text_input = RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_PASSWORD
        self.enter_text_to_field(locator_text_input, password_value)

    def enter_password_confirm(self, password_confirm_value):
        locator_text_input = RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_PASSWORD_CONFIRM
        self.enter_text_to_field(locator_text_input, password_confirm_value)

    def click_to_register_button(self):
        return self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_BUTTON_REGISTER).click()

    def get_header_h1_text(self):
        return self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_H1).text

    def get_meta_error_message(self) -> list:
        error_message_text = []
        for element in self.find_elements(RegisterPageLocators.LOCATOR_REGISTER_PAGE_META_ERROR):
            error_message_text.append(element.text)
        return error_message_text

    def clear_registration_form(self):
        registration_form = [
            self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME),
            self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_LAST_NAME),
            self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_USER_NAME),
            self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_PASSWORD),
            self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_PASSWORD_CONFIRM)
        ]

        for field in registration_form:
            field.send_keys(Keys.CONTROL + "a")
            field.send_keys(Keys.DELETE)

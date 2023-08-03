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

    def open_register_form(self):
        self.go_to_site()

    def enter_first_name(self, first_name_value):
        first_name_field = self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME)
        first_name_field.send_keys(Keys.CONTROL + "a")
        first_name_field.send_keys(Keys.DELETE)
        first_name_field.send_keys(first_name_value)

    def enter_last_name(self, last_name_value):
        last_name_field = self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_LAST_NAME)
        last_name_field.send_keys(Keys.CONTROL + "a")
        last_name_field.send_keys(Keys.DELETE)
        last_name_field.send_keys(last_name_value)

    def enter_user_name(self, user_name_value):
        field_user_name = self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_USER_NAME)
        field_user_name.clear()
        field_user_name.send_keys(user_name_value)

    def enter_password(self, password_value):
        field_password = self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_PASSWORD)
        field_password.send_keys(Keys.CONTROL + "a")
        field_password.send_keys(Keys.DELETE)
        field_password.send_keys(password_value)

    def enter_password_confirm(self, password_confirm_value):
        field_password_confirm = self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_PASSWORD_CONFIRM)
        field_password_confirm.send_keys(Keys.CONTROL + "a")
        field_password_confirm.send_keys(Keys.DELETE)
        field_password_confirm.send_keys(password_confirm_value)

    def click_to_register_button(self):
        return self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_BUTTON_REGISTER).click()

    def clear_first_name_field(self):
        first_name_field = self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME)
        first_name_field.send_keys(Keys.CONTROL + "a")
        first_name_field.send_keys(Keys.DELETE)

    def clear_last_name_field(self):
        last_name_field = self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_LAST_NAME)
        last_name_field.send_keys(Keys.CONTROL + "a")
        last_name_field.send_keys(Keys.DELETE)

    def get_header_h1_text(self):
        return self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_H1).text

    def get_meta_error_message(self) -> list:
        error_message_text = []
        for element in self.find_elements(RegisterPageLocators.LOCATOR_REGISTER_PAGE_META_ERROR):
            error_message_text.append(element.text)
        return error_message_text

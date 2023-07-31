from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPageLocators:
    LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME = (By.NAME, 'firstName')
    LOCATOR_REGISTER_PAGE_FIELD_LAST_NAME = (By.NAME, 'lastName')

    LOCATOR_REGISTER_PAGE_FIELD_USER_NAME = (By.ID, 'address')
    LOCATOR_REGISTER_PAGE_FIELD_PASSWORD = (By.ID, 'password')
    LOCATOR_REGISTER_PAGE_FIELD_PASSWORD_CONFIRM = (By.ID, 'password-confirm')

    LOCATOR_REGISTER_PAGE_BUTTON_REGISTER = (By.NAME, 'register')


class UserPage(BasePage):

    def enter_first_name(self, first_name_value):
        return self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME).send_keys(
            first_name_value)

    def enter_last_name(self, last_name_value):
        return self.find_element(RegisterPageLocators.LOCATOR_REGISTER_PAGE_FIELD_FIRST_NAME).send_keys(
            last_name_value)

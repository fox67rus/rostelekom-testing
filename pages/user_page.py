from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserPageLocators:
    LOCATOR_USER_PAGE_BUTTON_LOGOUT = (By.ID, 'logout-btn')
    LOCATOR_USER_PAGE_HEADER = (By.CLASS_NAME, 'card-container__title')


class UserPage(BasePage):

    def click_logout(self):
        return self.find_element(UserPageLocators.LOCATOR_USER_PAGE_BUTTON_LOGOUT).click()

    def get_header_text(self):
        return self.find_element(UserPageLocators.LOCATOR_USER_PAGE_HEADER).text

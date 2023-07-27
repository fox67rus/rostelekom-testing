from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserPageLocators:
    LOCATOR_USER_PAGE_TAB_PHONE = (By.ID, 'logout-btn')


class UserPage(BasePage):

    def click_logout(self):
        return self.find_element(UserPageLocators.LOCATOR_USER_PAGE_TAB_PHONE).click()

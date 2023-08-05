from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://b2c.passport.rt.ru/'
        self.base_phone = '88001000800'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not found {locator}')

    def enter_text_to_field(self, locator_text_input, value_to_input, defocusing_locator=(By.ID, 'app-footer')):
        """Метод для ввода текста в поле. После ввода происходит клик на элементе вне поля ввода,
        чтобы произошла обработка введенного текста"""
        field = self.find_element(locator_text_input)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(value_to_input)
        self.find_element(defocusing_locator).click()

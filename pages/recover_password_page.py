from selenium.webdriver.common.by import By
import allure
from data import Urls
from pages.base_page import BasePage


class RecoverPasswordPage(BasePage):
    RESET_PASSWORD_URL = Urls.RESET_PASSWORD_PAGE
    RECOVER_PASSWORD_URL = Urls.RECOVER_PASSWORD_PAGE
    RECOVER_PASSWORD_TEXT = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    EMAIL_INPUT_LOCATOR_ON_FORGOT_PASS_PAGE = (By.CSS_SELECTOR, 'div.input input.text.input__textfield')
    RECOVER_PASSWORD_BUTTON = (By.XPATH, '//button[contains(text(), "Восстановить")]')
    SHOW_HIDE_PASSWORD_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
    PASSWORD_FIELD_LOCATOR_FOCUSED = (By.XPATH,
                                      '//label[contains(@class, "input__placeholder") and contains(text(), "Пароль") '
                                      'and contains(@class, "input__placeholder-focused")]')
    PASSWORD_FIELD_LOCATOR_ACTIVE = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default '
                                               'input_status_active"]')

    @allure.step('Вводим email в инпут восстановления пароля')
    def enter_text_recover_password_page(self, text):
        self.enter_text(self.EMAIL_INPUT_LOCATOR_ON_FORGOT_PASS_PAGE, text)

    @allure.step('Дожидаемся открытия страницы восстановления пароля')
    def wait_for_load_recover_password_page(self):
        self.wait_for_load_page(self.RECOVER_PASSWORD_URL)

    @allure.step('Дожидаемся открытия страницы сброса пароля')
    def wait_for_load_reset_password_page(self):
        self.wait_for_load_page(self.RESET_PASSWORD_URL)

    @allure.step('Открываем страницу восстановления пароля')
    def open_recover_password_page(self):
        self.open_page(self.RECOVER_PASSWORD_URL)

    @allure.step('Кликаем на кнопку "Восстановить"')
    def click_recover_password_button(self):
        self.click_element(self.RECOVER_PASSWORD_BUTTON)

    @allure.step('Кликаем на кнопку "Показать/скрыть пароль"')
    def click_show_hide_password_button(self):
        self.click_element(self.SHOW_HIDE_PASSWORD_ICON)

    @allure.step('Ожидаем, что поле пароля станет активным')
    def wait_and_find_active_password_field(self):
        element = self.wait_and_find_element(self.PASSWORD_FIELD_LOCATOR_ACTIVE)
        return element

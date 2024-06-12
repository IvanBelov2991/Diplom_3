from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class RecoverPasswordPage(BasePage):
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

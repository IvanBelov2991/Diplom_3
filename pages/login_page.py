from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_TEXT_ENTER = (By.XPATH, '//h2[contains(text(), "Вход")]')
    RECOVER_PASSWORD_HYPERLINK_TEXT = (By.XPATH, '//a[text()="Восстановить пароль"]')
    RECOVER_PASSWORD_TEXT = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    EMAIL_INPUT = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')
    PASSWORD_INPUT = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]/input['
                                '@class="text input__textfield text_type_main-default" and @type="password" and '
                                '@name="Пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[contains(@class, "button_button_type_primary") and contains(@class, '
                              '"button_button_size_medium") and text()="Войти"]')
    PERSONAL_ACCOUNT_LINK = (By.XPATH, '//p[contains(@class, "AppHeader_header__linkText__3q_va") and contains('
                                       '@class, "ml-2") and text()="Личный Кабинет"]')
    PERSONAL_ACCOUNT_HISTORY = (By.XPATH,
                                '//a[contains(@class, "Account_link__2ETsJ") and contains(@class, '
                                '"text_type_main-medium") and contains(@class, "text_color_inactive") and text('
                                ')="История заказов"]')
    LOGOUT_BUTTON = (By.XPATH,
                     '//li[contains(@class, "Account_listItem__35dAP")]/button[contains(@class, '
                     '"Account_button__14Yp3") and contains(@class, "text_type_main-medium") and contains(@class, '
                     '"text_color_inactive") and text()="Выход"]')
    ORDER_HISTORY_LIST = (By.XPATH,
                          '//ul[contains(@class, "OrderHistory_profileList__374GU")]')
    ORDER_IN_HISTORY_LIST = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem__2x95r")]')
    ID_ORDER_IN_HISTORY_LIST = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and contains(@class, 'mb-10') and contains(@class, 'mt-5')]")
    CROSS_MODAL_HISTORY_ORDER = (By.XPATH,
                                 '//div[@class="Modal_orderBox__1xWdi"]//button['
                                 '@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')

    @allure.step('Вводим email в инпут на странице логина')
    def enter_email_on_login_page(self, text):
        self.enter_text(self.EMAIL_INPUT, text)

    @allure.step('Вводим пароль в инпут на странице логина')
    def enter_password_on_login_page(self, text):
        self.enter_text(self.PASSWORD_INPUT, text)

    @allure.step('Кликаем на последний заказ в "Истории заказов"')
    def click_last_order_element(self):
        order_history_list = self.get_visible_element(self.ORDER_HISTORY_LIST)
        order_elements = order_history_list.find_elements(*self.ORDER_IN_HISTORY_LIST)
        last_order_element = order_elements[len(order_elements) - 1]
        self.scroll_to_element(last_order_element)
        last_order_element.click()

    @allure.step('Находим id заказа в "Истории Заказов"')
    def get_id_order_on_history_list(self):
        order_count_element = self.wait_and_find_element(self.ID_ORDER_IN_HISTORY_LIST)
        order_count_text = order_count_element.text
        order_count = int(order_count_text.replace("#", ""))
        return order_count

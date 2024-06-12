import allure
from data import Urls, UserData
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPasswordPage:

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Переходим на страницу восстановления пароля, вводим почту,'
                        ' кликаем "Восстановить" - проверяем переход на страницу с паролем')
    def test_input_on_recover_password_page(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(Urls.RECOVER_PASSWORD_PAGE)
        recover_password_page.wait_for_load_page(Urls.RECOVER_PASSWORD_PAGE)
        recover_password_page.enter_text_recover_password_page(UserData.EMAIL)
        recover_password_page.click_element(recover_password_page.RECOVER_PASSWORD_BUTTON)
        recover_password_page.wait_for_load_page(Urls.RESET_PASSWORD_PAGE)
        assert driver.current_url == Urls.RESET_PASSWORD_PAGE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Переходим на страницу восстановления пароля, вводим почту,'
                        ' кликаем "Восстановить" - кликаем показать/скрыть пароль и проверяем статус поля')
    def test_button_on_reset_password_page(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_page(Urls.RECOVER_PASSWORD_PAGE)
        recover_password_page.wait_for_load_page(Urls.RECOVER_PASSWORD_PAGE)
        recover_password_page.enter_text_recover_password_page(UserData.EMAIL)
        recover_password_page.click_element(recover_password_page.RECOVER_PASSWORD_BUTTON)
        recover_password_page.wait_for_load_page(Urls.RESET_PASSWORD_PAGE)
        recover_password_page.click_element(recover_password_page.SHOW_HIDE_PASSWORD_ICON)

        password_field = recover_password_page.wait_and_find_element\
            (recover_password_page.PASSWORD_FIELD_LOCATOR_ACTIVE)
        assert password_field.is_displayed()

import allure
from data import Urls, UserData
from pages.recover_password_page import RecoverPasswordPage


class TestRecoverPasswordPage:

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Переходим на страницу восстановления пароля, вводим почту,'
                        ' кликаем "Восстановить" - проверяем переход на страницу с паролем')
    def test_input_on_recover_password_page(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_recover_password_page()
        recover_password_page.wait_for_load_recover_password_page()
        recover_password_page.enter_text_recover_password_page(UserData.EMAIL)
        recover_password_page.click_recover_password_button()
        recover_password_page.wait_for_load_reset_password_page()
        assert recover_password_page.RESET_PASSWORD_URL == Urls.RESET_PASSWORD_PAGE

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Переходим на страницу восстановления пароля, вводим почту,'
                        ' кликаем "Восстановить" - кликаем показать/скрыть пароль и проверяем статус поля')
    def test_button_on_reset_password_page(self, driver):
        recover_password_page = RecoverPasswordPage(driver)
        recover_password_page.open_recover_password_page()
        recover_password_page.wait_for_load_recover_password_page()
        recover_password_page.enter_text_recover_password_page(UserData.EMAIL)
        recover_password_page.click_recover_password_button()
        recover_password_page.wait_for_load_reset_password_page()
        recover_password_page.click_show_hide_password_button()
        recover_password_page.wait_and_find_active_password_field()
        assert recover_password_page.wait_and_find_active_password_field().is_displayed()

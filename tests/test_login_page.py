from pages.login_page import LoginPage
import allure
from data import Urls


class TestOpenRecoverPage:
    @allure.title('Проверка, что по клику на "Восстановить пароль" открывается страница восстановления пароля')
    @allure.description('Заходим на страницу логина и по клику на лого "Восстановить пароль"'
                        ' проваливаемся на страницу восстановления пароля,'
                        ' проверяем что находимся на странице восстановления пароля')
    def test_click_on_recover_password_button_show_recover_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_for_load_login_page()
        login_page.click_recover_password_link()
        login_page.wait_for_load_recover_password_page()
        login_page.wait_and_find_recover_password_text()
        assert login_page.RECOVER_PASSWORD_URL == Urls.RECOVER_PASSWORD_PAGE
        assert login_page.wait_and_find_recover_password_text() is not None


class TestLogin:
    @allure.title('Проверка логина')
    @allure.description('Заходим на страницу логина, вводим email и пароль, нажимаем кнопку "Войти"')
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_for_load_login_page()
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        login_page.wait_for_load_main_page()

        assert login_page.MAIN_PAGE_URL == Urls.MAIN_PAGE


class TestPersonalAccount:
    @allure.title('Проверка захода в личный кабинет')
    @allure.description('Заходим на страницу логина, вводим email и пароль,'
                        ' нажимаем кнопку "Войти", затем заходим в Личный кабинет')
    def test_enter_personal_account(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_for_load_login_page()
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        login_page.wait_for_load_main_page()
        login_page.click_personal_account_link()
        login_page.wait_for_load_personal_account_page()
        assert login_page.PERSONAL_ACCOUNT_URL == Urls.PERSONAL_ACCOUNT_PAGE

    @allure.title('Проверка захода в раздел "История заказов" в личном кабинете')
    @allure.description('Заходим на страницу логина, вводим email и пароль, нажимаем кнопку "Войти",'
                        ' затем заходим в раздел "История заказов" в Личном кабинете')
    def test_enter_personal_account_history(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_for_load_login_page()
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        login_page.wait_for_load_main_page()
        login_page.click_personal_account_link()
        login_page.wait_for_load_personal_account_page()
        login_page.click_personal_account_history()
        login_page.open_personal_account_history_page()
        assert login_page.PERSONAL_ACCOUNT_HISTORY_URL == Urls.PERSONAL_ACCOUNT_HISTORY_PAGE

    @allure.title('Проверка выхода из аккаунта в личном кабинете')
    @allure.description('Заходим на страницу логина, вводим email и пароль, нажимаем кнопку "Войти",'
                        ' затем заходим в Личный кабинет и выходим из аккаунта')
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_for_load_login_page()
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        login_page.wait_for_load_main_page()
        login_page.click_personal_account_link()
        login_page.wait_for_load_personal_account_page()
        login_page.click_logout_button()
        login_page.wait_for_load_login_page()
        assert login_page.LOGIN_URL == Urls.LOGIN_PAGE

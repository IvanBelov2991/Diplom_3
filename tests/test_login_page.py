from pages.login_page import LoginPage
import allure
from data import Urls, UserData


class TestOpenRecoverPage:
    @allure.title('Проверка, что по клику на "Восстановить пароль" открывается страница восстановления пароля')
    @allure.description('Заходим на страницу логина и по клику на лого "Восстановить пароль"'
                        ' проваливаемся на страницу восстановления пароля,'
                        ' проверяем что находимся на странице восстановления пароля')
    def test_click_on_recover_password_button_show_recover_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page.click_element(login_page.RECOVER_PASSWORD_HYPERLINK_TEXT)
        login_page.wait_for_load_page(Urls.RECOVER_PASSWORD_PAGE)
        login_page.wait_and_find_element(login_page.RECOVER_PASSWORD_TEXT)
        assert driver.current_url == Urls.RECOVER_PASSWORD_PAGE
        assert login_page.wait_and_find_element(login_page.RECOVER_PASSWORD_TEXT) is not None


class TestLogin:
    @allure.title('Проверка логина')
    @allure.description('Заходим на страницу логина, вводим email и пароль, нажимаем кнопку "Войти"')
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        login_page.wait_for_load_page(Urls.MAIN_PAGE)

        assert driver.current_url == Urls.MAIN_PAGE


class TestPersonalAccount:
    @allure.title('Проверка захода в личный кабинет')
    @allure.description('Заходим на страницу логина, вводим email и пароль,'
                        ' нажимаем кнопку "Войти", затем заходим в Личный кабинет')
    def test_enter_personal_account(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        login_page.wait_for_load_page(Urls.MAIN_PAGE)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_LINK)
        login_page.wait_for_load_page(Urls.PERSONAL_ACCOUNT_PAGE)
        assert driver.current_url == Urls.PERSONAL_ACCOUNT_PAGE

    @allure.title('Проверка захода в раздел "История заказов" в личном кабинете')
    @allure.description('Заходим на страницу логина, вводим email и пароль, нажимаем кнопку "Войти",'
                        ' затем заходим в раздел "История заказов" в Личном кабинете')
    def test_enter_personal_account_history(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        login_page.wait_for_load_page(Urls.MAIN_PAGE)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_LINK)
        login_page.wait_for_load_page(Urls.PERSONAL_ACCOUNT_PAGE)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_HISTORY)
        login_page.wait_for_load_page(Urls.PERSONAL_ACCOUNT_HISTORY_PAGE)
        assert driver.current_url == Urls.PERSONAL_ACCOUNT_HISTORY_PAGE

    @allure.title('Проверка выхода из аккаунта в личном кабинете')
    @allure.description('Заходим на страницу логина, вводим email и пароль, нажимаем кнопку "Войти",'
                        ' затем заходим в Личный кабинет и выходим из аккаунта')
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(Urls.LOGIN_PAGE)
        login_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        login_page.wait_for_load_page(Urls.MAIN_PAGE)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_LINK)
        login_page.wait_for_load_page(Urls.PERSONAL_ACCOUNT_PAGE)
        login_page.click_element(login_page.LOGOUT_BUTTON)
        login_page.wait_for_load_page(Urls.LOGIN_PAGE)
        assert driver.current_url == Urls.LOGIN_PAGE

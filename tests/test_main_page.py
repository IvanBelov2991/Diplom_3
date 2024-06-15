from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
from data import Urls


class TestMainPage:
    @allure.title('Клик по "Ленте Заказов" открывает страницу заказов')
    @allure.description('Проверка, что по клику на "Лента Заказов" открывается страница заказов')
    def test_click_on_order_list_open_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_load_main_page()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        assert main_page.ORDER_LIST_URL == Urls.ORDER_LIST_PAGE

    @allure.title('Клик по разделу "Конструктор" открывает страницу "Конструктор"')
    @allure.description('Проверка, что по клику на "Конструктор" открывается меню конструктора')
    def test_click_on_constructor_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_load_main_page()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        main_page.click_constructor_header()
        main_page.wait_for_load_main_page()
        main_page.wait_and_find_element_text_in_constructor()
        assert main_page.MAIN_PAGE_URL == Urls.MAIN_PAGE

    @allure.title('Клик на ингредиент "Флюоресцентная булка" открывает модальное окно ингредиента')
    @allure.description('В разделе конструктор кликаем на флюоресцентную булку, открывается модальное окно ингредиента')
    def test_click_on_ingredient_open_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_fluorescent_bun_pic()
        main_page.wait_and_find_modal_window_ingredient()
        assert main_page.wait_and_find_modal_window_ingredient().text == 'Детали ингредиента'

    @allure.title('Всплывающее окно ингредиента закрывается кликом по крестику')
    @allure.description('В разделе конструктор кликаем на флюоресцентную булку,'
                        ' открывается модальное окно ингредиента, закрываем его на крестик,'
                        ' проверяем, что модальное окно не отображается на экране')
    def test_close_modal_ingredient_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_fluorescent_bun_pic()
        main_page.wait_and_find_modal_window_ingredient()
        main_page.click_cross_modal_window()
        assert main_page.is_modal_window_ingredient_not_visible()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('В разделе конструктор переносим флюоресцентную булку в поле заказа,'
                        ' проверяем, что счетчик ингредиента увеличился')
    def test_count_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.drag_and_drop_fluorescent_bun_on_order_field()
        assert main_page.wait_and_find_element_count_fluorescent_bun().text == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Заходим на главную страницу, регистрируемся через кнопку "Войти в аккаунт",'
                        ' добавляем ингредиенты в поле, кликаем "Оформить заказ" проверяем,'
                        ' что появляется модальное окно о готовке заказа')
    def test_create_order_by_authorized_user(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_enter_account_button()
        main_page.wait_for_load_login_page()
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_fluorescent_bun_on_order_field()
        main_page.click_create_order_button()
        assert main_page.wait_and_find_element_order_has_started_to_prepare().text == \
               'Ваш заказ начали готовить'

    @allure.title('Клик на заказ в ленте заказов открывает всплывающее окно с деталями')
    @allure.description('Заходим на ленту заказов, кликаем на заказ в левом меню, проверяем текст на модальном окне')
    def test_click_order_on_order_list_open_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        main_page.click_order_on_order_list()
        main_page.wait_and_find_composition_text_on_modal_order_window()
        assert main_page.wait_and_find_composition_text_on_modal_order_window().text == 'Cостав'

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Заходим на ленту заказов, смотрим кол-во заказов в статусе "Выполнено за всё время",'
                        'создаем заказ и смотрим, что счетчик "Выполнено за всё время" увеличился')
    def test_count_orders_for_all_time_done(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_enter_account_button()
        main_page.wait_for_load_login_page()
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        main_page.wait_for_load_main_page()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        initial_order_count = main_page.get_order_count_orders_for_all_time_done()
        main_page.click_constructor_header()
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_fluorescent_bun_on_order_field()
        main_page.click_create_order_button()
        main_page.wait_and_find_element_order_has_started_to_prepare()
        main_page.click_cross_modal_preparing_burger()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        assert main_page.get_order_count_orders_for_all_time_done() == initial_order_count + 1

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Заходим на ленту заказов, смотрим кол-во заказов в статусе "Выполнено за сегодня",'
                        'создаем заказ и смотрим, что счетчик "Выполнено за сегодня" увеличился')
    def test_count_orders_for_today_done(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_enter_account_button()
        main_page.wait_for_load_login_page()
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        main_page.wait_for_load_main_page()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        initial_order_count = main_page.get_order_count_orders_done_for_today()
        main_page.click_constructor_header()
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_fluorescent_bun_on_order_field()
        main_page.click_create_order_button()
        main_page.wait_and_find_element_order_has_started_to_prepare()
        main_page.click_cross_modal_preparing_burger()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        assert main_page.get_order_count_orders_done_for_today() == initial_order_count + 1

    @allure.title('При создании нового заказа, заказ отображается на "Ленте заказов" в статусе "В работе"')
    @allure.description('Создаем заказ, запоминаем номер заказа, заходим на ленту заказов'
                        ' и проверяем что заказ с таким номером находится в статусе "В работе" ')
    def test_check_new_order_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_enter_account_button()
        main_page.wait_for_load_login_page()
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_fluorescent_bun_on_order_field()
        main_page.click_create_order_button()
        main_page.wait_and_find_element_order_has_started_to_prepare()
        main_page.is_element_tick_image_visible()
        main_page.is_element_loader_modal_window_not_visible()
        main_page.is_element_loader_modal_window_visible()
        main_page.is_element_id_order_visible()
        initial_order_count = main_page.get_id_order()
        main_page.click_cross_modal_preparing_burger()
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        assert main_page.get_id_order_status_in_work() == initial_order_count

    @allure.title('Заказ пользователя отображается на странице "История заказов"')
    @allure.description('Создаем заказа, заходим смотрим, что он отобразился в "Истории заказов"')
    def test_users_order_show_in_personal_history_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_enter_account_button()
        main_page.wait_for_load_login_page()
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_fluorescent_bun_on_order_field()
        main_page.click_create_order_button()
        main_page.wait_and_find_element_order_has_started_to_prepare()
        main_page.is_element_tick_image_visible()
        main_page.is_element_loader_modal_window_not_visible()
        main_page.is_element_id_order_visible()
        initial_order_count = main_page.get_id_order()
        main_page.click_cross_modal_preparing_burger()
        login_page.click_personal_account_link()
        login_page.click_personal_account_history()
        login_page.click_last_order_element()
        assert login_page.get_id_order_on_history_list() == initial_order_count

    @allure.title('Заказ пользователя из раздела «История заказов» отображаются на странице «Лента заказов"')
    @allure.description('Создаем заказа, заходим смотрим, что он отобразился в "Истории заказов"'
                        ' и на странице "Лента заказов"')
    def test_users_order_show_in_all_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_enter_account_button()
        main_page.wait_for_load_login_page()
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page()
        login_page.enter_password_on_login_page()
        login_page.click_login_button()
        main_page.wait_for_load_main_page()
        main_page.drag_and_drop_fluorescent_bun_on_order_field()
        main_page.click_create_order_button()
        main_page.wait_and_find_element_order_has_started_to_prepare()
        main_page.is_element_tick_image_visible()
        main_page.is_element_loader_modal_window_not_visible()
        main_page.is_element_id_order_visible()
        initial_order_count = main_page.get_id_order()
        main_page.click_cross_modal_preparing_burger()
        login_page.click_personal_account_link()
        login_page.click_personal_account_history()
        login_page.click_last_order_element()
        main_page.press_escape_key()
        # обошел крестик, так как не получилось найти локатор в DOM
        main_page.click_order_list_header()
        main_page.wait_for_load_order_list_page()
        login_page.click_element(login_page.ORDER_IN_HISTORY_LIST)
        assert login_page.get_id_order_on_history_list() == initial_order_count










    

from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
from data import Urls, UserData


class TestMainPage:
    @allure.title('Клик по "Ленте Заказов" открывает страницу заказов')
    @allure.description('Проверка, что по клику на "Лента Заказов" открывается страница заказов')
    def test_click_on_order_list_open_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        assert driver.current_url == Urls.ORDER_LIST_PAGE

    @allure.title('Клик по разделу "Конструктор" открывает страницу "Конструктор"')
    @allure.description('Проверка, что по клику на "Конструктор" открывается меню конструктора')
    def test_click_on_constructor_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        main_page.click_element(main_page.CONSTRUCTOR_LINK)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.wait_and_find_element(main_page.CONSTRUCTOR_PAGE_TEXT)
        assert driver.current_url == Urls.MAIN_PAGE

    @allure.title('Клик на ингредиент "Флюоресцентная булка" открывает модальное окно ингредиента')
    @allure.description('В разделе конструктор кликаем на флюоресцентную булку, открывается модальное окно ингредиента')
    def test_click_on_ingredient_open_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.FLUORESCENT_BUN_PIC)
        main_page.wait_and_find_element(main_page.MODAL_WINDOW_INGREDIENT)
        assert main_page.is_element_visible(main_page.MODAL_WINDOW_INGREDIENT)
        assert main_page.wait_and_find_element(main_page.MODAL_WINDOW_INGREDIENT).text == 'Детали ингредиента'

    @allure.title('Всплывающее окно ингредиента закрывается кликом по крестику')
    @allure.description('В разделе конструктор кликаем на флюоресцентную булку,'
                        ' открывается модальное окно ингредиента, закрываем его на крестик,'
                        ' проверяем, что модальное окно не отображается на экране')
    def test_close_modal_ingredient_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.FLUORESCENT_BUN_PIC)
        main_page.wait_and_find_element(main_page.MODAL_WINDOW_INGREDIENT)
        main_page.click_element(main_page.CROSS_MODAL_IGREDIENT_WINDOW)
        assert main_page.is_element_not_visible(main_page.MODAL_WINDOW_INGREDIENT)

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('В разделе конструктор переносим флюоресцентную булку в поле заказа,'
                        ' проверяем, что счетчик ингредиента увеличился')
    def test_count_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.drag_and_drop_element(main_page.FLUORESCENT_BUN_INGREDIENT, main_page.BURGER_CONSTRUCTOR_BASKET)
        assert main_page.wait_and_find_element(main_page.FLUORESCENT_BUN_INGREDIENT_COUNT).text == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Заходим на главную страницу, регистрируемся через кнопку "Войти в аккаунт",'
                        ' добавляем ингредиенты в поле, кликаем "Оформить заказ" проверяем,'
                        ' что появляется модальное окно о готовке заказа')
    def test_create_order_by_authorized_user(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ENTER_ACCOUNT_BUTTON)
        main_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.drag_and_drop_element(main_page.FLUORESCENT_BUN_INGREDIENT, main_page.BURGER_CONSTRUCTOR_BASKET)
        main_page.click_element(main_page.CREATE_ORDER_BUTTON)
        assert main_page.wait_and_find_element(main_page.YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT).text == \
               'Ваш заказ начали готовить'

    @allure.title('Клик на заказ в ленте заказов открывает всплывающее окно с деталями')
    @allure.description('Заходим на ленту заказов, кликаем на заказ в левом меню, проверяем текст на модальном окне')
    def test_click_order_on_order_list_open_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        main_page.click_element(main_page.ORDER_IN_ORDER_LIST)
        main_page.wait_and_find_element(main_page.COMPOSITION_TEXT_ON_MODAL_ORDER_WINDOW)
        assert main_page.wait_and_find_element(main_page.COMPOSITION_TEXT_ON_MODAL_ORDER_WINDOW).text == 'Cостав'

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description('Заходим на ленту заказов, смотрим кол-во заказов в статусе "Выполнено за всё время",'
                        'создаем заказ и смотрим, что счетчик "Выполнено за всё время" увеличился')
    def test_count_orders_for_all_time_done(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ENTER_ACCOUNT_BUTTON)
        main_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        initial_order_count = main_page.get_order_count_orders_for_all_time_done()
        main_page.click_element(main_page.CONSTRUCTOR_LINK)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.drag_and_drop_element(main_page.FLUORESCENT_BUN_INGREDIENT, main_page.BURGER_CONSTRUCTOR_BASKET)
        main_page.click_element(main_page.CREATE_ORDER_BUTTON)
        main_page.wait_and_find_element(main_page.YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT)
        main_page.click_element(main_page.CLOSE_MODAL_WINDOW_PRERARING_BURGER)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        assert main_page.get_order_count_orders_for_all_time_done() == initial_order_count + 1

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description('Заходим на ленту заказов, смотрим кол-во заказов в статусе "Выполнено за сегодня",'
                        'создаем заказ и смотрим, что счетчик "Выполнено за сегодня" увеличился')
    def test_count_orders_for_today_done(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ENTER_ACCOUNT_BUTTON)
        main_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        initial_order_count = main_page.get_order_count_orders_done_for_today()
        main_page.click_element(main_page.CONSTRUCTOR_LINK)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.drag_and_drop_element(main_page.FLUORESCENT_BUN_INGREDIENT, main_page.BURGER_CONSTRUCTOR_BASKET)
        main_page.click_element(main_page.CREATE_ORDER_BUTTON)
        main_page.wait_and_find_element(main_page.YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT)
        main_page.wait_and_find_element(main_page.CLOSE_MODAL_WINDOW_PRERARING_BURGER)
        main_page.click_element(main_page.CLOSE_MODAL_WINDOW_PRERARING_BURGER)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        assert main_page.get_order_count_orders_done_for_today() == initial_order_count + 1

    @allure.title('При создании нового заказа, заказ отображается на "Ленте заказов" в статусе "В работе"')
    @allure.description('Создаем заказ, запоминаем номер заказа, заходим на ленту заказов'
                        ' и проверяем что заказ с таким номером находится в статусе "В работе" ')
    def test_check_new_order_in_work(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ENTER_ACCOUNT_BUTTON)
        main_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.drag_and_drop_element(main_page.FLUORESCENT_BUN_INGREDIENT, main_page.BURGER_CONSTRUCTOR_BASKET)
        main_page.click_element(main_page.CREATE_ORDER_BUTTON)
        main_page.wait_and_find_element(main_page.YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT)
        main_page.is_element_visible(main_page.TICK_IMAGE_ON_MODAL_WINDOW)
        main_page.is_element_not_visible(main_page.MODAL_WINDOW_LOADING_IMAGE)
        main_page.is_element_visible(main_page.MODAL_WINDOW_INGREDIENT_ID)
        initial_order_count = main_page.get_id_order()
        main_page.click_element(main_page.CLOSE_MODAL_WINDOW_PRERARING_BURGER)
        main_page.wait_and_find_element(main_page.ORDER_LIST)
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        assert main_page.get_id_order_status_in_work() == initial_order_count

    @allure.title('Заказ пользователя отображается на странице "История заказов"')
    @allure.description('Создаем заказа, заходим смотрим, что он отобразился в "Истории заказов"')
    def test_users_order_show_in_personal_history_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ENTER_ACCOUNT_BUTTON)
        main_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.drag_and_drop_element(main_page.FLUORESCENT_BUN_INGREDIENT, main_page.BURGER_CONSTRUCTOR_BASKET)
        main_page.click_element(main_page.CREATE_ORDER_BUTTON)
        main_page.wait_and_find_element(main_page.YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT)
        main_page.is_element_visible(main_page.TICK_IMAGE_ON_MODAL_WINDOW)
        main_page.is_element_not_visible(main_page.MODAL_WINDOW_LOADING_IMAGE)
        main_page.is_element_visible(main_page.MODAL_WINDOW_INGREDIENT_ID)
        initial_order_count = main_page.get_id_order()
        main_page.click_element(main_page.CLOSE_MODAL_WINDOW_PRERARING_BURGER)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_LINK)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_HISTORY)
        login_page.click_last_order_element()
        assert login_page.get_id_order_on_history_list() == initial_order_count

    @allure.title('Заказ пользователя из раздела «История заказов» отображаются на странице «Лента заказов"')
    @allure.description('Создаем заказа, заходим смотрим, что он отобразился в "Истории заказов"'
                        ' и на странице "Лента заказов"')
    def test_users_order_show_in_all_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.click_element(main_page.ENTER_ACCOUNT_BUTTON)
        main_page.wait_for_load_page(Urls.LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.enter_email_on_login_page(UserData.EMAIL)
        login_page.enter_password_on_login_page(UserData.PASSWORD)
        login_page.click_element(login_page.LOGIN_BUTTON)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.drag_and_drop_element(main_page.FLUORESCENT_BUN_INGREDIENT, main_page.BURGER_CONSTRUCTOR_BASKET)
        main_page.click_element(main_page.CREATE_ORDER_BUTTON)
        main_page.wait_and_find_element(main_page.YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT)
        main_page.is_element_visible(main_page.TICK_IMAGE_ON_MODAL_WINDOW)
        main_page.is_element_not_visible(main_page.MODAL_WINDOW_LOADING_IMAGE)
        main_page.is_element_visible(main_page.MODAL_WINDOW_INGREDIENT_ID)
        initial_order_count = main_page.get_id_order()
        main_page.click_element(main_page.CLOSE_MODAL_WINDOW_PRERARING_BURGER)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_LINK)
        login_page.click_element(login_page.PERSONAL_ACCOUNT_HISTORY)
        login_page.click_last_order_element()
        main_page.press_escape_key()
        # обошел крестик, так как не получилось найти локатор в DOM
        main_page.click_element(main_page.ORDER_LIST)
        main_page.wait_for_load_page(Urls.ORDER_LIST_PAGE)
        main_page.click_element(login_page.ORDER_IN_HISTORY_LIST)
        assert login_page.get_id_order_on_history_list() == initial_order_count










    

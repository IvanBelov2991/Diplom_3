import time
from selenium.webdriver.common.by import By
import allure
from data import Urls
from pages.base_page import BasePage


class MainPage(BasePage):
    ORDER_LIST_URL = Urls.ORDER_LIST_PAGE
    MAIN_PAGE_URL = Urls.MAIN_PAGE
    LOGIN_PAGE_URL = Urls.LOGIN_PAGE

    ORDER_LIST = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]')
    CONSTRUCTOR_LINK = (By.XPATH,
                        '//p[contains(@class, "AppHeader_header__linkText__3q_va") and contains(@class, "ml-2") and text()="Конструктор"]')
    CONSTRUCTOR_PAGE_TEXT = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")
    FLUORESCENT_BUN_PIC = (By.XPATH, '//img[@src="https://code.s3.yandex.net/react/code/bun-01.png"]')
    FLUORESCENT_BUN_INGREDIENT = (By.XPATH,
                                  '//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    FLUORESCENT_BUN_INGREDIENT_COUNT = (By.XPATH, '//p[@class="counter_counter__num__3nue1"]')
    MODAL_WINDOW_INGREDIENT = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_modified__3Hjkd")]')
    CROSS_MODAL_IGREDIENT_WINDOW = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    CREATE_ORDER_BUTTON = (By.XPATH,
                           '//button[contains(@class, "button_button__33qZ0") and contains(@class, "button_button_type_primary__1O7Bx") and contains(@class, "button_button_size_large__G21Vg") and text()="Оформить заказ"]')
    ENTER_ACCOUNT_BUTTON = (By.XPATH,
                            '//button[contains(@class, "button_button__33qZ0") and contains(@class, "button_button_type_primary__1O7Bx") and contains(@class, "button_button_size_large__G21Vg") and text()="Войти в аккаунт"]')
    YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT = (By.XPATH,
                                                 '//p[contains(@class, "undefined") and contains(@class, "text") and contains(@class, "text_type_main-small") and contains(@class, "mb-2")]')
    ORDER_IN_ORDER_LIST = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem__2x95r") and contains(@class, "mb-6")]')
    COMPOSITION_TEXT_ON_MODAL_ORDER_WINDOW = (By.XPATH,
                                              '//p[contains(@class, "text") and contains(@class, "text_type_main-medium") and contains(@class, "mb-8")]')
    ORDERS_DONE_FOR_ALL_TIME = (By.XPATH, '//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    CLOSE_MODAL_WINDOW_PRERARING_BURGER = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]')
    ORDERS_DONE_FOR_TODAY = (By.XPATH, '//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    MODAL_WINDOW_INGREDIENT_ID = (By.XPATH,
                                  '//h2[contains(@class, "Modal_modal__title_shadow__3ikwq") and contains(@class, "Modal_modal__title__2L34m")]')
    ID_ORDERS_IN_WORK = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li.text.text_type_digits-default')
    TICK_IMAGE_ON_MODAL_WINDOW = (By.XPATH, '//img[contains(@src, "./static/media/tick.887b83be.gif")]')
    MODAL_WINDOW_LOADING_IMAGE = (By.XPATH,
                                  '//img[contains(@src, "./static/media/loading.89540200.svg") and contains(@class, "Modal_modal__loading__3534A")]')

    @allure.step('Находим элемент "Выполнено за все время" в ленте заказов')
    def wait_and_find_element_orders_for_all_time_done(self):
        element = self.wait_and_find_element(self.ORDERS_DONE_FOR_ALL_TIME)
        return element

    @allure.step('Находим количество заказов "Выполнено за все время"')
    def get_order_count_orders_for_all_time_done(self):
        order_count_element = self.wait_and_find_element_orders_for_all_time_done()
        order_count = int(order_count_element.text)
        return order_count

    @allure.step('Кликаем на раздел "Лента заказов" в хеадере')
    def click_order_list_header(self):
        self.click_element(self.ORDER_LIST)

    @allure.step('Кликаем на раздел "Конструктор" в хеадере')
    def click_constructor_header(self):
        self.click_element(self.CONSTRUCTOR_LINK)

    @allure.step('Кликаем на ингредиент "Флюоресцентная булка"')
    def click_fluorescent_bun_pic(self):
        self.click_element(self.FLUORESCENT_BUN_PIC)

    @allure.step('Кликаем на кнопку "Войти в аккаунт"')
    def click_enter_account_button(self):
        self.click_element(self.ENTER_ACCOUNT_BUTTON)

    @allure.step('Кликаем на кнопку "Оформить заказ"')
    def click_create_order_button(self):
        self.click_element(self.CREATE_ORDER_BUTTON)

    @allure.step('Ожидаем открытие модального окна ингредиента')
    def wait_and_find_modal_window_ingredient(self):
        element = self.wait_and_find_element(self.MODAL_WINDOW_INGREDIENT)
        return element

    @allure.step('Ожидаем текст в модальном окне - "Ваш заказ начали готовить"')
    def wait_and_find_element_order_has_started_to_prepare(self):
        element = self.wait_and_find_element(self.YOUR_ORDER_HAS_STARTED_TO_PREPARE_ELEMENT)
        return element

    @allure.step('Ожидаем текст в модальном окне - "Состав"')
    def wait_and_find_composition_text_on_modal_order_window(self):
        element = self.wait_and_find_element(self.COMPOSITION_TEXT_ON_MODAL_ORDER_WINDOW)
        return element

    @allure.step('Кликаем на заказ в списке заказов')
    def click_order_on_order_list(self):
        self.click_element(self.ORDER_IN_ORDER_LIST)

    @allure.step('Кликаем крестик и закрываем окно "Ваш бургер начали готовить"')
    def click_cross_modal_preparing_burger(self):
        self.click_element(self.CLOSE_MODAL_WINDOW_PRERARING_BURGER)

    @allure.step('Кликаем на крестик и закрываем модальное окно ингредиента')
    def click_cross_modal_window(self):
        self.click_element(self.CROSS_MODAL_IGREDIENT_WINDOW)

    @allure.step('Находим элемент "Соберите бургер" в разделе "Конструктор')
    def wait_and_find_element_text_in_constructor(self):
        self.wait_and_find_element(self.CONSTRUCTOR_PAGE_TEXT)

    @allure.step('Открываем основную страницу - main_page')
    def open_main_page(self):
        self.open_page(self.MAIN_PAGE_URL)

    @allure.step('Дожидаемся открытия основной страницы - main_page')
    def wait_for_load_main_page(self):
        self.wait_for_load_page(self.MAIN_PAGE_URL)

    @allure.step('Дожидаемся открытия страницы логина')
    def wait_for_load_login_page(self):
        self.wait_for_load_page(self.LOGIN_PAGE_URL)

    @allure.step('Дожидаемся открытия раздела "Лента заказов"')
    def wait_for_load_order_list_page(self):
        self.wait_for_load_page(self.ORDER_LIST_URL)

    @allure.step('Находим элемент "Выполнено за сегодня" в ленте заказов')
    def wait_and_find_element_orders_done_for_today(self):
        element = self.wait_and_find_element(self.ORDERS_DONE_FOR_TODAY)
        return element

    @allure.step('Находим элемент счетчик у ингредиента "Флюоресцентная булка"')
    def wait_and_find_element_count_fluorescent_bun(self):
        element = self.wait_and_find_element(self.FLUORESCENT_BUN_INGREDIENT_COUNT)
        return element

    @allure.step('Находим количество заказов "Выполнено за сегодня"')
    def get_order_count_orders_done_for_today(self):
        order_count_element = self.wait_and_find_element_orders_done_for_today()
        order_count = int(order_count_element.text)
        return order_count

    @allure.step("Проверяем, что модальное окно ингредиента не отображается")
    def is_modal_window_ingredient_not_visible(self):
        self.is_element_not_visible(self.MODAL_WINDOW_INGREDIENT)
        return True

    @allure.step("Проверяем, что галочка прогрузки отображается на модальном окне приготовления бургера")
    def is_element_tick_image_visible(self):
        element = self.is_element_visible(self.TICK_IMAGE_ON_MODAL_WINDOW)
        return element

    @allure.step("Проверяем, что галочка прогрузки не отображается на модальном окне приготовления бургера")
    def is_element_tick_image_not_visible(self):
        element = self.is_element_not_visible(self.TICK_IMAGE_ON_MODAL_WINDOW)
        return element

    @allure.step("Проверяем, что лоадер прогрузки не отображается на модальном окне приготовления бургера")
    def is_element_loader_modal_window_not_visible(self):
        element = self.is_element_not_visible(self.MODAL_WINDOW_LOADING_IMAGE)
        return element

    @allure.step("Проверяем, что лоадер прогрузки отображается на модальном окне приготовления бургера")
    def is_element_loader_modal_window_visible(self):
        element = self.is_element_visible(self.MODAL_WINDOW_LOADING_IMAGE)
        return element

    @allure.step("Проверяем, что id заказа отображается на модальном окне приготовления бургера")
    def is_element_id_order_visible(self):
        element = self.is_element_visible(self.MODAL_WINDOW_INGREDIENT_ID)
        return element

    @allure.step('Находим количество заказов "Выполнено за сегодня"')
    def get_order_count_orders_done_for_today(self):
        order_count_element = self.wait_and_find_element_orders_done_for_today()
        order_count = int(order_count_element.text)
        return order_count

    @allure.step('Находим id заказа')
    def get_id_order(self):
        def is_valid_order_id(order_id):
            return order_id != 9999 and len(str(order_id)) == 5

        order_id_element = self.wait_and_find_element(self.MODAL_WINDOW_INGREDIENT_ID)
        order_id = int(order_id_element.text)

        retry_count = 0
        max_retries = 5
        while not is_valid_order_id(order_id) and retry_count < max_retries:
            time.sleep(1)
            order_id_element = self.wait_and_find_element(self.MODAL_WINDOW_INGREDIENT_ID)
            order_id = int(order_id_element.text)
            retry_count += 1

        if retry_count == max_retries:
            raise Exception("Не получилось достать валидный id после нескольких попыток")

        return order_id

    @allure.step('Находим id заказа в статусе "В работе"')
    def get_id_order_status_in_work(self):
        order_count_element = self.wait_and_find_element(self.ID_ORDERS_IN_WORK)
        order_count_text = order_count_element.text
        if order_count_text.isdigit():
            order_count = int(order_count_text)
        else:
            order_count = 0
        return order_count

    @allure.step('Перетаскиваем элемент "Флюоресцентная булка" в поле заказа')
    def drag_and_drop_fluorescent_bun_on_order_field(self):
        self.drag_and_drop_element(self.FLUORESCENT_BUN_INGREDIENT, self.BURGER_CONSTRUCTOR_BASKET)

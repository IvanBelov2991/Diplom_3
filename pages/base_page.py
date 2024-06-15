import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти на странице элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Дождаться отображения элемента')
    def is_element_visible(self, locator):
        try:
            element = self.wait_and_find_element(locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    @allure.step('Дождаться, что элемент исчезнет со страницы')
    def is_element_not_visible(self, locator):
        try:
            self.wait_and_find_element(locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Найти на странице все элементы локатора')
    def wait_and_find_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(locator))
        return elements

    @allure.step('Дожидаемся загрузки страницы')
    def wait_for_load_page(self, url):
        WebDriverWait(self.driver, timeout=5).until(expected_conditions.url_to_be(url))

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Вводим текст в инпут')
    def enter_text(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        text_element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", text_element)

    @allure.step('Переключение на вкладку')
    def switch_to_page(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for_load_page(url)

    @allure.step('Подтверждение нахождения на странице')
    def assert_current_page(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Ожидаемый URL '{expected_url}', находимся на '{actual_url}'"

    @allure.step('Подтверждение нахождения на странице по частичному совпадению в url')
    def assert_partial_url_in_current_url(self, partial_url):
        assert partial_url in self.driver.current_url, "URL не содержит partial_url"

    @allure.step('Перетащить элемент в целевое поле')
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.wait_and_find_element(source_locator)
        target_element = self.wait_and_find_element(target_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(source_element, target_element).perform()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ожидание отображения элемента')
    def get_visible_element(self, locator):
        try:
            element = self.wait_and_find_element(locator)
            return element
        except NoSuchElementException:
            return None

    def press_escape_key(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ESCAPE)

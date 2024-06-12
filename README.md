# Diplom_3
pages:
base_page.py - общие методы
login_page.py - методы на странице логина (включая персональный кабинет)
main_page.py - методы для работы на основной странице (конструктор и лента заказов)
recover_password_page.py - методы для работы на странице восстановления пароля

tests:
conftest.py - фикстура
test_login_page.py - тесты на логин
test_main.page.py - тесты на главной странице
test_recover_password_page.py - тесты для проверки посстановления пароля

data.py - данные для тестов (urls и данные для логина)
allure-results - результаты прогона тестов
requirements.txt - библиотеки для импорта
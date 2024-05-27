# Для фикстур можно задавать область покрытия фикстур. Допустимые значения:
# “function” (фикстура будет вызываться один раз для тестового метода),
# “class” (один раз для класса),
# “module” (один раз для модуля),
# “session” (один раз для всех тестов, запущенных в данной сессии).
# Запустим все тесты из класса TestMainPage1 в одном браузере, задав scope="class" в фикстуре browser:

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
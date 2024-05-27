import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"

       # Cоздание экземпляра браузера и его закрытие только один раз для всех тестов тест-сьюта
class TestMainPage1():
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()
    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()
    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    # создание браузера для каждого теста в тест-сьюте
class TestMainPage2():
    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()
    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()
    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

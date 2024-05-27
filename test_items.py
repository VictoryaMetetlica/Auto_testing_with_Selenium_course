from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно
# проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/. Тест должен
# запускаться с параметром language следующей командой: pytest --language=es test_items.py

def test_visibility_add_button(browser):
        # переход на нужную страницу
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        # поиск кнопки добавления товара в корзину
    add_to_basket_btn = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located(('class name', 'btn-add-to-basket')))
    assert add_to_basket_btn, 'Страница не содержит кнопку добавления в корзину'
    time.sleep(30)
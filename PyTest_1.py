# запустить тесты из unittest_1 с помощью PyTest. В выводе найдите последнюю строку, скопируйте её и отправьте в это
# задание. Отправьте текст, который находится между  === и ===. PS предупреждений (warnings) в ответе быть не должно.

import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# оформить тесты из unic_selector.py в стиле unittest. Создайте новый файл Создайте в нем класс с тестами, который должен
# наследоваться от unittest.TestCase Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html Оформите финальные
# проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual Запустите получившиеся тесты из файла
# Просмотрите отчёт о запуске и найдите последнюю строчку  Отправьте эту строчку в качестве ответа на это задание


def test_first_registration():
    browser.get("http://suninjuly.github.io/registration1.html")
    browser.find_element('css selector', ".first_block .form-control.first").send_keys("first name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.second").send_keys("last name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.third").send_keys("email@mail.ru")
    time.sleep(1)
    browser.find_element('css selector', "button.btn").click()
    time.sleep(1)
        # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element('tag name', "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert 'Congratulations! You have successfully registered!' == welcome_text, 'expected text != actual text'


def test_second_registration():
    browser.get("http://suninjuly.github.io/registration2.html")
    browser.find_element('css selector', ".first_block .form-control.first").send_keys("first name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.second").send_keys("last name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.third").send_keys("email@mail.ru")
    time.sleep(1)
    browser.find_element('css selector', "button.btn").click()
    time.sleep(1)
        # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert 'Congratulations! You have successfully registered!' == welcome_text, 'expected text != actual text'


if __name__ == "__main__":
    pytest.main()
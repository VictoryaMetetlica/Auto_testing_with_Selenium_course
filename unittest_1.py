import unittest
import time

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


def link_t(link):
    browser.get(link)

    browser.find_element('css selector', ".first_block .form-control.first").send_keys("first name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.second").send_keys("last name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.third").send_keys("email@mail.ru")
    time.sleep(1)
    browser.find_element('css selector', "button.btn").click()

    time.sleep(1)
    return browser.find_element('tag name', "h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "Registration is failed")


    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "Registration is failed")

if __name__ == "__main__":
    unittest.main()

import json
import time

import pytest
from selenium import webdriver


# чтобы не передавать в git мои логин/пароль, предварительно создала в проекте json файл 'my_stepik_data.json'
    # и добавила его в gitignore.py

    # импортируем библиотеку json и создаем фикстуру, которая вернет словарь логин/пароль из файла my_stepik_data.json:
@pytest.fixture(scope="session")
def load_config():
    # Открываем файл 'my_stepik_data.json' с конфигом в режиме чтения
    with open('my_stepik_data.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        # вернуть словарь из логина и пароля
        return config

class TestLogin:
                # фикстура browser находится в корневом каталоге conftest.py и запускается оттуда
             # авторизация на странице
    def test_authorization(self, browser, load_config):
        link = 'https://stepik.org/lesson/236895/step/1'
        browser.get(link)
            # лицезреть действия
        time.sleep(2)
            # находим кнопку Войти и и кликаем по ней
        browser.find_element('css selector', '.st-link.st-link_style_button').click()
            # записываем в переменные логин/пароль
        login = load_config['login_stepik']
        password = load_config['password_stepik']
            # находим поле логина и вводим его
        browser.find_element('css selector', "#id_login_email").send_keys(login)
            # находим поле пароля и вводим его
        browser.find_element('css selector', "#id_login_password").send_keys(password)
            # находим кнопку Войти и кликаем по ней
        browser.find_element('css selector', '.sign-form__btn.button_with-loader').click()
            # лицезреть действия
        time.sleep(5)
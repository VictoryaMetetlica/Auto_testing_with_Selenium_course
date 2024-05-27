# параметризация тестов: Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
# Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать
# автотест со следующим сценарием действий:
#     открыть страницу
#     авторизоваться на странице со своим логином и паролем (см. test_stepik_login)
#     ввести правильный ответ (поле перед вводом должно быть пустым)
#     нажать кнопку "Отправить"
#     дождаться фидбека о том, что ответ правильный
#     проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
# Опциональный фидбек — это текст в черном поле. Правильным ответом на задачу в заданных шагах является число:
# answer = math.log(int(time.time()))
# Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1
# Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали
# стабильно. В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает
# со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import json

# чтобы не передавать в git мои логин/пароль, в проекте предварительно создала json файл 'my_stepik_data.json'
    # и добавила его в файл gitignore.py
    # импортируем библиотеку json и создаем фикстуру, которая вернет словарь логин/пароль из файла my_stepik_data.json:
@pytest.fixture(scope="session")
def load_config():
    # Открываем файл 'my_stepik_data.json' с конфигом в режиме чтения
    with open('my_stepik_data.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        # вернуть словарь из логина и пароля
        return config

    # введем переменную для дальнейшей конкатенации кусочков ответа
message = ''
        # в качестве аргументов передаётся изменяемая часть ссылок
@pytest.mark.parametrize('part_of_link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_links(browser, load_config, part_of_link):
    answer = math.log(int(time.time()))
    browser.get(f'https://stepik.org/lesson/{part_of_link}/step/1')
        # вводим результат answer в поле ввода
    enter_field = browser.find_element('css selector', '.string-quiz__textarea')
    enter_field.clear()
    enter_field.send_keys(str(answer))
        # кликаем по кнопке Отправить
    send_button_field = ('css selector', '.st-link.st-link_style_button')
    send_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(send_button_field))
    send_button.click()
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
    time.sleep(2)
    result = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(('css selector', 'p.smart-hints__hint'))).text
    # для красивой записи ответа использовала оператор if, чтобы ответ был в строчку и его не искать по упавшим тестам
    # assert result == 'Correct!', f'message is:   {result}'
        # указываем global - ранее заведенную переменную, чтобы использовать ее в этой функции
    global message
    if result != 'Correct!':
        message += result
        print(f'\ntext for answer:   {message}')


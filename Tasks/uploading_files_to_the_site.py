import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Открыть страницу http://suninjuly.github.io/file_input.html Заполнить текстовые поля: имя, фамилия, email.
# Загрузить файл. Файл должен иметь расширение.txt и может быть пустым. Нажать кнопку "Submit". Если все сделано быстро
# (в задаче ограничение по времени), вы увидите окно с числом - это ответ к задаче.

    # Открыть страницу http://suninjuly.github.io/file_input.html
driver.get("http://suninjuly.github.io/file_input.html")
    # создадим локаторы для каждого поля ввода и кнопки
first_name_locator = ('xpath', '//input[@name="firstname"]')
last_name_locator = ('xpath', '//input[@name="lastname"]')
email_locator = ('xpath', '//input[@name="email"]')
browse_locator = ('xpath', '//input[@id="file"]')
submit_locator = ('xpath', '//button[@class="btn btn-primary"]')
    # Заполнить текстовые поля
name_field = driver.find_element(*first_name_locator).send_keys('Viktoria')
last_name_field = driver.find_element(*last_name_locator).send_keys('Metelica')
email_field = driver.find_element(*email_locator).send_keys('viv_kutas@mail.ru')
browse_field = driver.find_element(*browse_locator)
    # создадим пустой файл автоматически
# with open("file_example.txt", "w") as file:
#    content = file.write("automationbypython")  # create test.txt file (создаст в папке, где скрипт)
    # создаём файл без содержимого, если отсутствует - для этого далее его удалим, чтоб при перезапуске все работало
open("file_example.txt", 'a').close()
    # определим путь к данному файлу
current_path = os.path.abspath(os.path.dirname(__file__))
    # записать в переменную имя файла с расширением
file_name = "file_example.txt"
    # объединить путь и имя файла
file_path = os.path.join(current_path, file_name)
    # внести полный путь к файлу по кнопке browse - рядом с кнопкой browse появится имя файла
browse_field.send_keys(file_path)
    # удалим созданный файл file_example.txt
os.remove("file_example.txt")
    # Нажать кнопку "Submit"
driver.find_element(*submit_locator).click()
time.sleep(5)
    # вывести результат сообщения (алерта), который появляется после нажатия на Submit, на экран
print('число для ответа: ', driver.switch_to.alert.text.split()[-1])
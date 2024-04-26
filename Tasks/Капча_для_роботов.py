import math
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()


  # Задание: кликаем по checkboxes и radiobuttons (капча для роботов): Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x. Посчитать математическую функцию от x. Ввести ответ # в текстовое поле. Отметить
# checkbox "I'm the robot". Выбрать radiobutton "Robots rule!". Нажать на кнопку Submit. # Если все сделано правильно и
# достаточно быстро (в задаче ограничение по времени), вы увидите окно с числом - это ответ к задаче.


driver.get('https://suninjuly.github.io/math.html')
    # Считать значение для переменной x.
x_element = driver.find_element('xpath', '//span[@id="input_value"]')
x = x_element.text
print('значение х для раcчета:', x)
    # Посчитать математическую функцию от x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

    # Ввести ответ в текстовое поле.
y = calc(x)
print('рассчитанное значение у:', y)
answer_field_locator = ('xpath', '//input[@id="answer"]')
answer_field = driver.find_element(*answer_field_locator)
answer_field.send_keys(y)
    # Отметить checkbox "I'm the robot".
checkbox_locator = ('xpath', '//input[@id="robotCheckbox"]')
checkbox = driver.find_element(*checkbox_locator)
checkbox.click()
    # Выбрать radiobutton "Robots rule!".
radiobutton_locator = ('xpath', '//input[@id="robotsRule"]')
radiobutton = driver.find_element(*radiobutton_locator)
radiobutton.click()
    # Нажать на кнопку Submit.
submit_locator = ('xpath', '//button[@type="submit"]')
submit_button = driver.find_element(*submit_locator)
submit_button.click()
  # вывести результат сообщения (алерта), который появляется после нажатия на Submit, на экран
print(driver.switch_to.alert.text)
time.sleep(5)
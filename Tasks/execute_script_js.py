import math
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Открыть страницу https://SunInJuly.github.io/execute_script.html. Считать значение для переменной x. Посчитать
# математическую функцию от x. Проскроллить страницу вниз в область видимости элементов, перекрытых футером. Ввести
# ответ в текстовое поле. Выбрать checkbox "I'm the robot". Переключить radiobutton "Robots rule!". Нажать кнопку
# "Submit". Если все сделано быстро (в задаче ограничение по времени), вы увидите окно с числом - это ответ к задаче.

driver.get('https://SunInJuly.github.io/execute_script.html')
x_locator = ('xpath', '//span[@id ="input_value"]')
answer_field = ('xpath', '//input[@id="answer"]')
checkbox_locator = ('xpath', '//input[@id="robotCheckbox"]')
radiobutton_locator = ('xpath', '//input[@id="robotsRule"]')
    # Считать значение для переменной x
x = driver.find_element(*x_locator).text
print('x = ', x)
    # Посчитать математическую функцию от x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
print('рассчитанное значение у:', y)
    # Ввести ответ в текстовое поле
answer = driver.find_element(*answer_field)
    # Проскроллить страницу вниз в область видимости элементa answer, перекрытых футером.
driver.execute_script('return arguments[0].scrollIntoView(true);', answer)
answer.send_keys(y)
driver.find_element(*answer_field).send_keys(Keys.ENTER)
    # Выбрать checkbox "I'm the robot"
checkbox = driver.find_element(*checkbox_locator)
    # Проскроллить страницу вниз в область видимости элементa checkbox, перекрытых футером.
driver.execute_script('return arguments[0].scrollIntoView(true);', checkbox)
checkbox.click()
time.sleep(2)
    # Переключить radiobutton "Robots rule!"
radiobutton = driver.find_element(*radiobutton_locator)
   # Проскроллить страницу вниз в область видимости элементa radiobutton, перекрытых футером.
driver.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
radiobutton.click()
    # Нажать на кнопку Submit.
submit_locator = ('xpath', '//button[@type="submit"]')
submit_button = driver.find_element(*submit_locator)
   # Проскроллить страницу вниз в область видимости элементa Submit, перекрытых футером.
driver.execute_script('return arguments[0].scrollIntoView(true);', submit_button)
submit_button.click()
    # вывести результат сообщения (алерта), который появляется после нажатия на Submit, на экран
print('число для ответа: ', driver.switch_to.alert.text.split()[-1])
time.sleep(2)


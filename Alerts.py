import time
import math

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
    # создается обьект wait:
wait = WebDriverWait(driver, 30, poll_frequency=1)
driver.maximize_window()

# Открыть страницу http://suninjuly.github.io/alert_accept.html Нажать на кнопку Принять confirm На новой странице
# решить капчу для роботов, чтобы получить число с ответом. Если все сделано быстро (в задаче ограничение по времени),
# вы увидите окно с числом - это ответ к задаче.

    # Открыть страницу http://suninjuly.github.io/alert_accept.html
driver.get('http://suninjuly.github.io/alert_accept.html')
    # Нажать на кнопку
driver.find_element('xpath', '//button[@class="btn btn-primary"]').click()
    # Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
confirm = wait.until(EC.alert_is_present())
    # Переключение на alert
driver.switch_to.alert
    # Нажать на кнопку Принять confirm
confirm.accept()
    # сделаем скриншот, чтоб понять задачу
driver.save_screenshot('task.png')
    # На новой странице решить капчу для роботов, чтобы получить число с ответом
x = driver.find_element('xpath', '//span[@id="input_value"]').text
print('значение х для раcчета:', x)
    # Посчитать математическую функцию от x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

    # Ввести ответ в текстовое поле.
y = calc(x)
print('рассчитанное значение у:', y)
driver.find_element('xpath', '//input[@id="answer"]').send_keys(y)
    # нажать на submit
driver.find_element('xpath', '//button[@class="btn btn-primary"]').click()
  # вывести результат сообщения (алерта), который появляется после нажатия на Submit, на экран
print('числовой ответ', driver.switch_to.alert.text.split()[-1])
time.sleep(3)
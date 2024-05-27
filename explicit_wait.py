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
wait = WebDriverWait(driver, 12, poll_frequency=1)
driver.maximize_window()

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html Дождаться, когда цена дома уменьшится до $100
# (ожидание нужно установить не меньше 12 секунд) Нажать на кнопку "Book" Решить уже известную нам математическую
# задачу (используйте ранее написанный код) и отправить решение

    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
driver.get('http://suninjuly.github.io/explicit_wait2.html')
    # Дождаться, когда цена дома уменьшится до $100
price = ('xpath', '//h5[@id="price"]')
button = wait.until(EC.text_to_be_present_in_element(price, '$100'))
    # Нажать на кнопку "Book"
book_button = driver.find_element('xpath', '//button[@id="book"]').click()
    # решить капчу для роботов, чтобы получить число с ответом
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
driver.find_element('xpath', '//button[@id="solve"]').click()
  # вывести результат сообщения (алерта), который появляется после нажатия на Submit, на экран
print('числовой ответ', wait.until(EC.alert_is_present()).driver.switch_to.alert.text.split()[-1])
time.sleep(2)
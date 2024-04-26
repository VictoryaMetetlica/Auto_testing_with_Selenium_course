import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
# from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# dropdown = Select(driver.find_element('tag name', 'select'))

# Открыть страницу https://suninjuly.github.io/selects1.html Посчитать сумму заданных чисел Выбрать в выпадающем
# списке значение равное расчитанной сумме Нажать кнопку "Submit"

    # Открыть страницу https://suninjuly.github.io/selects1.html
driver.get('https://suninjuly.github.io/selects1.html')
    # Задать локаторы для работы
num_locator_1 = ("xpath", "//span[@id='num1']")
num_locator_2 = ("xpath", "//span[@id='num2']")
    # Взять значения из локаторов
num_1 = int(driver.find_element(*num_locator_1).text)
num_2 = int(driver.find_element(*num_locator_2).text)
y = num_1 + num_2
    # Выбрать в выпадающем списке значение равное расчитанной сумме - выполнила через ввод числа в поле
select_field = driver.find_element('tag name', 'select')
select_field.send_keys(str(y))
select_field.send_keys(Keys.ENTER)
time.sleep(2)
    # Нажать кнопку "Submit"
sub_locator = ('xpath', '//button[@class="btn btn-default"]')
driver.find_element(*sub_locator).click()
  # вывести результат сообщения (алерта), который появляется после нажатия на Submit, на экран
print(driver.switch_to.alert.text.split()[-1])
time.sleep(5)
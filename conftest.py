from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
import pytest

# Настроим тестовые окружения с помощью передачи параметров через командную строку. Сначала добавляем в файле conftest
# обработчик опции в функции pytest_addoption, затем напишем фикстуру request, которая будет обрабатывать переданные в
# опции данные


    # Обработчик опции выбора браузера (chrome or firefox) и языка страницы
def pytest_addoption(parser):
        # задаем опцию для запуска "браузер": если не указать, то запускается Chrome
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
        # задаем опцию для запуска "язык": ru, en, fr
    parser.addoption('--language', action='store', default='ru', help="Choose language name to select: 'ru', 'en', 'fr'..")


    # фикстура запуска и закрытия браузера с выбором языка
@pytest.fixture(scope="function")
def browser(request):
        # считываем данные: язык и браузер (если есть)
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        print(f'user language: {user_language}')
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        print(f'user language: {user_language}')
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


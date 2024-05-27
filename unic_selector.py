import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def link_t(link):
    browser.get(link)

    browser.find_element('css selector', ".first_block .form-control.first").send_keys("first name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.second").send_keys("last name")
    time.sleep(1)
    browser.find_element('css selector', ".first_block .form-control.third").send_keys("email@mail.ru")
    time.sleep(3)
    browser.find_element('css selector', "button.btn").click()

    time.sleep(1)
    return browser.find_element('tag name', "h1").text

links = ['http://suninjuly.github.io/registration1.html', 'http://suninjuly.github.io/registration2.html']

for link in links:
    link_t(link)
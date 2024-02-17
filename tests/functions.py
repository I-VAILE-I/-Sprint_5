from selenium import webdriver
from tests.locators import Links


def registered_user():
    return ['andrew', 'andrew_5_000@ya.ru', '123456']


def Driver():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1280,720')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get(Links.get_link)
    return driver
import random
import pytest
from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def open_main_page():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1280,720')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get('https://stellarburgers.nomoreparties.site')
    return driver


@pytest.fixture()
def open_personal_cabinet():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1280,720')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    return driver


@pytest.fixture()
def open_registration():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1280,720')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
    return driver


@pytest.fixture()
def registered_user():
    return ['andrew', 'andrew_5_000@ya.ru', '123456']


@pytest.fixture()
def correct_login_and_password():
    login_lst = []
    name = f'andrew_5_{random.randint(100, 999)}'
    login = f'{name}@ya.ru'
    login_lst.append(name)
    login_lst.append(login)
    login_lst.append(str(random.randint(100000, 999999)))
    return login_lst
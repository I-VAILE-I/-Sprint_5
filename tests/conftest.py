import pytest
from selenium.webdriver.common.by import By
from locators import Xpath, LinkText
from functions import registered_user
from selenium import webdriver

# используется во всех остальных тестах
@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1280,720')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.close()


# используется только в трех тестах, убрал все остальные фикстуры, которые использовались по 1 разу
@pytest.fixture()
def login_and_open_personal_cabinet_to_registered_user():
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--window-size=1280,720')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
    driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
    driver.find_element(By.XPATH, Xpath.login_button).click()
    yield driver
    driver.close()

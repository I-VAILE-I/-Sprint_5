import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Xpath, LinkText, Links
from tests.helpers import correct_login_and_password
from tests.functions import registered_user, Driver


@pytest.fixture()
def open_main_page():
    driver = Driver()
    yield driver
    driver.close()


@pytest.fixture()
def open_main_page_and_change_section_to_sauces():
    driver = Driver()
    driver.find_element(By.XPATH, Xpath.section_sauces).click()
    yield driver
    driver.close()


@pytest.fixture()
def open_main_page_and_change_section_to_fillings():
    driver = Driver()
    driver.find_element(By.XPATH, Xpath.section_fillings).click()
    yield driver
    driver.close()


@pytest.fixture()
def open_main_page_and_login():
    driver = Driver()
    driver.find_element(By.XPATH, Xpath.login_button_on_main_page).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(Links.login_link))
    driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
    driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
    driver.find_element(By.XPATH, Xpath.login_button).click()
    yield driver
    driver.close()


@pytest.fixture()
def login_and_open_personal_cabinet_to_registered_user():
    driver = Driver()
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
    driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
    driver.find_element(By.XPATH, Xpath.login_button).click()
    yield driver
    driver.close()


@pytest.fixture()
def login_with_incorrect_password():
    driver = Driver()
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
    driver.find_element(By.XPATH, Xpath.login_input_password).send_keys('1')
    driver.find_element(By.XPATH, Xpath.login_button).click()
    yield driver
    driver.close()


@pytest.fixture()
def login_from_recovery_passwqord_page():
    driver = Driver()
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.forgot_password_button).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(Links.forgot_password))
    driver.find_element(By.XPATH, Xpath.login_button_on_recovery_password_page).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(Links.login_link))
    driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
    driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
    driver.find_element(By.XPATH, Xpath.login_button).click()
    yield driver
    driver.close()


@pytest.fixture()
def open_registration():
    driver = Driver()
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.open_registration_on_login_page).click()
    yield driver
    driver.close()


@pytest.fixture()
def open_registration_and_register_user():
    registration_and_data = correct_login_and_password()
    driver = Driver()
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.open_registration_on_login_page).click()
    driver.find_element(By.XPATH, Xpath.registration_input_name).send_keys(registration_and_data[0])
    driver.find_element(By.XPATH, Xpath.registration_input_email).send_keys(registration_and_data[1])
    driver.find_element(By.XPATH, Xpath.registration_input_password).send_keys(registration_and_data[2])
    driver.find_element(By.XPATH, Xpath.click_on_registration_button).click()
    yield driver, registration_and_data
    driver.close()


@pytest.fixture()
def open_registration_and_register_user_with_incorrect_password():
    registration_and_data = correct_login_and_password()
    driver = Driver()
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.open_registration_on_login_page).click()
    driver.find_element(By.XPATH, Xpath.registration_input_name).send_keys(registration_and_data[0])
    driver.find_element(By.XPATH, Xpath.registration_input_email).send_keys(registration_and_data[1])
    driver.find_element(By.XPATH, Xpath.registration_input_password).send_keys('1')
    driver.find_element(By.XPATH, Xpath.click_on_registration_button).click()
    yield driver
    driver.close()


@pytest.fixture()
def open_registration_click_on_login_button():
    driver = Driver()
    driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
    driver.find_element(By.XPATH, Xpath.open_registration_on_login_page).click()
    driver.find_element(By.XPATH, Xpath.login_button_on_registration_page).click()
    WebDriverWait(driver, 3).until(EC.url_to_be(Links.login_link))
    driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
    driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
    driver.find_element(By.XPATH, Xpath.login_button).click()
    yield driver
    driver.close()

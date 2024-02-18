from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers import correct_login_and_password
from locators import Xpath, LinkText


class TestRegistrationUser:

    def test_registeration_with_correct_email_and_password_and_logout(
            self,
            driver
    ):
        name_email_password = correct_login_and_password()
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        driver.find_element(By.XPATH, Xpath.open_registration_on_login_page).click()
        driver.find_element(By.XPATH, Xpath.registration_input_name).send_keys(name_email_password[0])
        driver.find_element(By.XPATH, Xpath.registration_input_email).send_keys(name_email_password[1])
        driver.find_element(By.XPATH, Xpath.registration_input_password).send_keys(name_email_password[2])
        driver.find_element(By.XPATH, Xpath.click_on_registration_button).click()
        WebDriverWait(driver, 25).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

        driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(name_email_password[1])
        driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(name_email_password[2])
        driver.find_element(By.XPATH, Xpath.login_button).click()

        WebDriverWait(driver, 25).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 25).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(By.XPATH, Xpath.login_logout_button).click()

        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_with_incorrect_password(
            self,
            driver
    ):
        name_email_password = correct_login_and_password()
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        driver.find_element(By.XPATH, Xpath.open_registration_on_login_page).click()
        driver.find_element(By.XPATH, Xpath.registration_input_name).send_keys(name_email_password[0])
        driver.find_element(By.XPATH, Xpath.registration_input_email).send_keys(name_email_password[1])
        driver.find_element(By.XPATH, Xpath.registration_input_password).send_keys('1')
        driver.find_element(By.XPATH, Xpath.click_on_registration_button).click()
        assert driver.find_element(By.XPATH, Xpath.error_input).text == 'Некорректный пароль'

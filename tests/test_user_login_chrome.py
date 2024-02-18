from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from functions import registered_user
from locators import Xpath, LinkText


class TestLoginUser:

    def test_login_open_personal_cabinet_and_logout(
            self,
            login_and_open_personal_cabinet_to_registered_user
    ):
        driver = login_and_open_personal_cabinet_to_registered_user
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(By.XPATH, Xpath.login_logout_button).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_error_login_with_incorrect_password(
            self,
            driver
    ):
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
        driver.find_element(By.XPATH, Xpath.login_input_password).send_keys('1')
        driver.find_element(By.XPATH, Xpath.login_button).click()
        assert driver.find_element(By.XPATH, Xpath.error_input).text == 'Некорректный пароль'

    def test_click_on_login_button_on_main_page(
            self,
            driver
    ):
        driver.find_element(By.XPATH, Xpath.login_button_on_main_page).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
        driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
        driver.find_element(By.XPATH, Xpath.login_button).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_on_login_button_in_registration_page(
            self,
            driver
    ):
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        driver.find_element(By.XPATH, Xpath.open_registration_on_login_page).click()
        driver.find_element(By.XPATH, Xpath.login_button_on_registration_page).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
        driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
        driver.find_element(By.XPATH, Xpath.login_button).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_on_login_button_in_password_recovery_page(
            self,
            driver
    ):
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        driver.find_element(By.XPATH, Xpath.forgot_password_button).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password"))
        driver.find_element(By.XPATH, Xpath.login_button_on_recovery_password_page).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(registered_user()[1])
        driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(registered_user()[2])
        driver.find_element(By.XPATH, Xpath.login_button).click()
        WebDriverWait(driver, 3).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_open_personal_cabinet_and_go_to_main_page(
            self,
            login_and_open_personal_cabinet_to_registered_user
    ):
        driver = login_and_open_personal_cabinet_to_registered_user
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 35).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
        driver.find_element(By.XPATH, Xpath.main_page_logo).click()
        WebDriverWait(driver, 25).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_open_personal_cabinet_and_go_to_constructor(
            self,
            login_and_open_personal_cabinet_to_registered_user
    ):
        driver = login_and_open_personal_cabinet_to_registered_user
        WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        driver.find_element(By.XPATH, Xpath.constructor_selection).click()
        WebDriverWait(driver, 25).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

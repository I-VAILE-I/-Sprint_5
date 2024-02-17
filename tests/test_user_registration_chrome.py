from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Xpath, LinkText, Links


class TestRegistrationUser:

    def test_registeration_with_correct_email_and_password_and_logout(
            self,
            open_registration_and_register_user
    ):
        driver = open_registration_and_register_user[0]
        correct_login_and_password = open_registration_and_register_user[1]
        WebDriverWait(driver, 25).until(EC.url_to_be(Links.login_link))
        assert driver.current_url == Links.login_link

        driver.find_element(By.XPATH, Xpath.login_input_email).send_keys(correct_login_and_password[1])
        driver.find_element(By.XPATH, Xpath.login_input_password).send_keys(correct_login_and_password[2])
        driver.find_element(By.XPATH, Xpath.login_button).click()

        WebDriverWait(driver, 25).until(EC.url_to_be(Links.main_page))
        assert driver.current_url == Links.main_page

        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 25).until(EC.url_to_be(Links.profile))
        driver.find_element(By.XPATH, Xpath.login_logout_button).click()

        WebDriverWait(driver, 3).until(EC.url_to_be(Links.login_link))
        assert driver.current_url == Links.login_link

    def test_registration_with_incorrect_password(
            self,
            open_registration_and_register_user_with_incorrect_password
    ):
        assert open_registration_and_register_user_with_incorrect_password.find_element(By.XPATH, Xpath.error_input).text == 'Некорректный пароль'

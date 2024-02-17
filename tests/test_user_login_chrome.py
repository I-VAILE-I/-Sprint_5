from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Xpath, LinkText, Links


class TestLoginUser:

    def test_login_open_personal_cabinet_and_logout(
            self,
            login_and_open_personal_cabinet_to_registered_user
    ):
        driver = login_and_open_personal_cabinet_to_registered_user
        WebDriverWait(driver, 3).until(EC.url_to_be(Links.main_page))
        assert driver.current_url == Links.main_page

        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Links.profile))
        driver.find_element(By.XPATH, Xpath.login_logout_button).click()
        WebDriverWait(driver, 3).until(EC.url_to_be(Links.login_link))
        assert driver.current_url == Links.login_link

    def test_error_login_with_incorrect_password(
            self,
            login_with_incorrect_password
    ):
        driver = login_with_incorrect_password
        assert driver.find_element(By.XPATH, Xpath.error_input).text == 'Некорректный пароль'

    def test_click_on_login_button_on_main_page(
            self,
            open_main_page_and_login
    ):
        driver = open_main_page_and_login
        WebDriverWait(driver, 3).until(EC.url_to_be(Links.main_page))
        assert driver.current_url == Links.main_page

    def test_click_on_login_button_in_registration_page(
            self,
            open_registration_click_on_login_button
    ):
        driver = open_registration_click_on_login_button
        WebDriverWait(driver, 3).until(EC.url_to_be(Links.main_page))
        assert driver.current_url == Links.main_page

    def test_click_on_login_button_in_password_recovery_page(
            self,
            login_from_recovery_passwqord_page
    ):
        driver = login_from_recovery_passwqord_page
        WebDriverWait(driver, 3).until(EC.url_to_be(Links.main_page))
        assert driver.current_url == Links.main_page

    def test_open_personal_cabinet_and_go_to_main_page(
            self,
            login_and_open_personal_cabinet_to_registered_user
    ):
        driver = login_and_open_personal_cabinet_to_registered_user
        WebDriverWait(driver, 10).until(EC.url_to_be(Links.main_page))
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 35).until(EC.url_to_be(Links.profile))
        assert driver.current_url == Links.profile
        driver.find_element(By.XPATH, Xpath.main_page_logo).click()
        WebDriverWait(driver, 25).until(EC.url_to_be(Links.main_page))
        assert driver.current_url == Links.main_page

    def test_open_personal_cabinet_and_go_to_constructor(
            self,
            login_and_open_personal_cabinet_to_registered_user
    ):
        driver = login_and_open_personal_cabinet_to_registered_user
        WebDriverWait(driver, 15).until(EC.url_to_be(Links.main_page))
        driver.find_element(By.LINK_TEXT, LinkText.personal_cabinet).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Links.profile))
        driver.find_element(By.XPATH, Xpath.constructor_selection).click()
        WebDriverWait(driver, 25).until(EC.url_to_be(Links.main_page))
        assert driver.current_url == Links.main_page

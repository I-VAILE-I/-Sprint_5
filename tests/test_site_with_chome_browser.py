import time
from selenium.webdriver.common.by import By


class TestSiteWithChomeBrowser:

    def test_registeration_with_correct_email_and_password_and_logout(
            self,
            correct_login_and_password: list,
            open_registration
    ):

        open_registration.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']").send_keys(correct_login_and_password[0])
        open_registration.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']").send_keys(correct_login_and_password[1])
        open_registration.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(correct_login_and_password[2])
        open_registration.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        time.sleep(1)
        assert open_registration.current_url == 'https://stellarburgers.nomoreparties.site/login'

        open_registration.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]').send_keys(correct_login_and_password[1])
        open_registration.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(correct_login_and_password[2])
        open_registration.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        time.sleep(1)
        assert open_registration.current_url == 'https://stellarburgers.nomoreparties.site/'

        open_registration.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        time.sleep(0.5)
        open_registration.find_element(By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()

        open_registration.close()

    def test_open_personal_cabinet_and_logout(
            self,
            registered_user: list,
            open_personal_cabinet
    ):
        open_personal_cabinet.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]').send_keys(registered_user[1])
        open_personal_cabinet.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(registered_user[2])
        open_personal_cabinet.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        time.sleep(3)
        assert open_personal_cabinet.current_url == 'https://stellarburgers.nomoreparties.site/'

        open_personal_cabinet.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        time.sleep(0.5)
        open_personal_cabinet.find_element(By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()

        open_personal_cabinet.close()

    def test_main_page_change_sections(
            self,
            registered_user: list,
            open_main_page
    ):
        open_main_page.find_element(By.XPATH, "//span[text()='Соусы']").click()
        time.sleep(0.5)
        assert open_main_page.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text == 'Соусы'
        open_main_page.find_element(By.XPATH, "//span[text()='Начинки']").click()
        time.sleep(0.5)
        assert open_main_page.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text == 'Начинки'
        open_main_page.find_element(By.XPATH, "//span[text()='Булки']").click()
        time.sleep(0.5)
        assert open_main_page.find_element(By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']").text == 'Булки'
        open_main_page.close()

    def test_registration_with_incorrect_password(
            self,
            correct_login_and_password: list,
            open_registration
    ):
        open_registration.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]').send_keys(correct_login_and_password[1])
        open_registration.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('1')
        open_registration.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        open_registration.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']")
        assert open_registration.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'

        open_registration.close()

    def test_error_login_with_incorrect_password(
            self,
            registered_user: list,
            open_personal_cabinet
    ):
        open_personal_cabinet.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]').send_keys(registered_user[1])
        open_personal_cabinet.find_element(By.XPATH, "//input[@name='Пароль']").send_keys('1')
        open_personal_cabinet.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        open_personal_cabinet.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']")
        assert open_personal_cabinet.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'

        open_personal_cabinet.close()

    def test_click_on_login_button_on_main_page(
            self,
            registered_user: list,
            open_main_page
    ):
        open_main_page.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
        time.sleep(1)
        open_main_page.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]').send_keys(registered_user[1])
        open_main_page.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(registered_user[2])
        open_main_page.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        time.sleep(4)
        assert open_main_page.current_url == 'https://stellarburgers.nomoreparties.site/'

        open_main_page.close()

    def test_click_on_login_button_in_registration_page(
            self,
            registered_user: list,
            open_registration
    ):
        open_registration.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
        time.sleep(1)
        open_registration.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]').send_keys(registered_user[1])
        open_registration.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(registered_user[2])
        open_registration.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        time.sleep(2)
        assert open_registration.current_url == 'https://stellarburgers.nomoreparties.site/'

        open_registration.close()

    def test_click_on_login_button_in_password_recovery_page(
            self,
            registered_user: list,
            open_personal_cabinet
    ):
        open_personal_cabinet.find_element(By.XPATH, "//a[@href='/forgot-password']").click()
        time.sleep(0.5)
        open_personal_cabinet.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj']").click()
        time.sleep(0.5)
        open_personal_cabinet.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@name="name"]').send_keys(registered_user[1])
        open_personal_cabinet.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(registered_user[2])
        open_personal_cabinet.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        time.sleep(3)
        assert open_personal_cabinet.current_url == 'https://stellarburgers.nomoreparties.site/'

        open_personal_cabinet.close()

    def test_open_personal_cabinet_and_go_to_main_page(
            self,
            open_personal_cabinet
    ):
        time.sleep(0.5)
        assert open_personal_cabinet.current_url == 'https://stellarburgers.nomoreparties.site/login'
        open_personal_cabinet.find_element(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']").click()
        assert open_personal_cabinet.current_url == 'https://stellarburgers.nomoreparties.site/'
        time.sleep(0.5)
        open_personal_cabinet.close()

    def test_open_personal_cabinet_and_go_to_constructor(
            self,
            open_personal_cabinet
    ):
        time.sleep(3)
        open_personal_cabinet.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2']").click()
        time.sleep(3)
        open_personal_cabinet.close()

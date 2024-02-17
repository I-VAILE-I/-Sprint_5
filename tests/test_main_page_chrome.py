from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Xpath


class TestMainPageChangeSections:
    def test_main_page_change_sections_to_sauces(
            self,
            open_main_page_and_change_section_to_sauces
    ):
        driver = open_main_page_and_change_section_to_sauces
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Соусы'))
        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Соусы'

    def test_main_page_change_sections_to_fillings(
            self,
            open_main_page_and_change_section_to_fillings
    ):
        driver = open_main_page_and_change_section_to_fillings
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Начинки'))
        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Начинки'

    def test_main_page_change_sections_from_fillings_to_rolls(
            self,
            open_main_page_and_change_section_to_fillings
    ):
        driver = open_main_page_and_change_section_to_fillings
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Начинки'))
        driver.find_element(By.XPATH, Xpath.section_rolls).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Булки'))

        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Булки'

    def test_main_page_change_sections_from_sauces_to_rolls(
            self,
            open_main_page_and_change_section_to_sauces
    ):
        driver = open_main_page_and_change_section_to_sauces
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Соусы'))
        driver.find_element(By.XPATH, Xpath.section_rolls).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Булки'))
        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Булки'

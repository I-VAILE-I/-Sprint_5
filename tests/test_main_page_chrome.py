from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import Xpath


class TestMainPageChangeSections:
    def test_main_page_change_sections_to_sauces(
            self,
            driver
    ):
        driver.find_element(By.XPATH, Xpath.section_sauces).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Соусы'))
        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Соусы'

    def test_main_page_change_sections_to_fillings(
            self,
            driver
    ):
        driver.find_element(By.XPATH, Xpath.section_fillings).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Начинки'))
        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Начинки'

    def test_main_page_change_sections_from_fillings_to_rolls(
            self,
            driver
    ):
        driver.find_element(By.XPATH, Xpath.section_fillings).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Начинки'))
        driver.find_element(By.XPATH, Xpath.section_rolls).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Булки'))

        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Булки'

    def test_main_page_change_sections_from_sauces_to_rolls(
            self,
            driver
    ):
        driver.find_element(By.XPATH, Xpath.section_sauces).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Соусы'))
        driver.find_element(By.XPATH, Xpath.section_rolls).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, Xpath.active_section), 'Булки'))
        assert driver.find_element(By.XPATH, Xpath.active_section).text == 'Булки'

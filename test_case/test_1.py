import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_object.BasePage import BasePage
from Page_object.HomePage import HomePage
from Page_object.ElementPage import ElementPage


@allure.title("Testcase 01: Verify file download functionality")
def test_testcase_01():
    with allure.step("Initializing WebDriver"):
        driver = webdriver.Chrome()
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        element_page = ElementPage(driver)

    with allure.step("Opening the website"):
        driver.get("https://demoqa.com/")

    with allure.step("Performing actions on the page"):
        wait = WebDriverWait(driver, 10)

        home_page.click_element_button()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-1"]/span')))

        element_page.click_checkbox_button()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')))

        element_page.click_home_directory_button()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')))

        downloads_button = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
        driver.execute_script("arguments[0].scrollIntoView();", downloads_button)

        element_page.click_downloads_directory_button()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')))

        element_page.click_word_file_button()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[3]')))

    with allure.step("Verifying the downloaded file"):
        result_text = driver.find_element(By.XPATH, '//*[@id="result"]/span[2]').text
        assert "wordFile" in result_text, f"Expected 'wordFile' in '{result_text}'"

    with allure.step("Closing the browser"):
        driver.quit()

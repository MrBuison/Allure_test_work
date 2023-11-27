from Page_object.BasePage import BasePage
from selenium.webdriver.common.by import By


class ElementPage(BasePage):
    def click_checkbox_button(self):
        check_box_button = self.driver.find_element(By.XPATH, '//*[@id="item-1"]/span')
        check_box_button.click()

    def click_home_directory_button(self):
        home_directory_button = self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/button')
        home_directory_button.click()

    def click_downloads_directory_button(self):
        downloads_directory_button = self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/button')
        downloads_directory_button.click()

    def click_word_file_button(self):
        word_file_button = self.driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[3]')
        word_file_button.click()

from Page_object.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def click_element_button(self):
        element_button = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]/h5')
        self.driver.execute_script("arguments[0].scrollIntoView();", element_button)
        element_button.click()



import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseComponent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Знайти елемент")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
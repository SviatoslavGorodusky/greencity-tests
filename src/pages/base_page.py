import os
from selenium.common.exceptions import StaleElementReferenceException
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.base_url = os.getenv("BASE_URL")

    def open(self):
        # Відкриває URL, який прописаний у твоєму .env
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def find_element(self, locator):
        # Додаємо ігнорування StaleElementReferenceException
        return WebDriverWait(self.driver, 15, ignored_exceptions=[StaleElementReferenceException]).until(
            EC.visibility_of_element_located(locator)
        )
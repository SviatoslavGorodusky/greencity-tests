import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent

class Header(BaseComponent):
    SEARCH_ICON = (By.XPATH, "//span[@class='search-img']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")

    @allure.step("Відкрити пошук та ввести текст: {text}")
    def perform_search(self, text):
        self.find_element(self.SEARCH_ICON).click()
        search_field = self.find_element(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)

    @allure.step("Виконати пошук: {text}")
    def perform_search(self, text):
        self.find_element(self.SEARCH_ICON).click()
        search_field = self.find_element(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)  # Симулюємо натискання клавіші Enter
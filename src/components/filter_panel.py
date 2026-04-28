import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.components.base_component import BaseComponent


class FilterPanel(BaseComponent):
    FILTER_TYPE_DROPDOWN = (By.XPATH,
                            "//div[contains(@class, 'dropdown') and .//mat-label[contains(text(),'Тип події')]]")
    OPTION_ECONOMIC = (By.XPATH, "//mat-option//span[contains(text(), 'Економічний')]")
    ACTIVE_FILTER_TAG = (By.XPATH, "//span[contains(@class, 'tag-active')]")
    FILTER_TITLE = (By.XPATH, "//h2[contains(text(), 'Фільтрувати')]")
    VIEW_LIST_BTN = (By.XPATH, "//button[contains(@class,'list')]")
    VIEW_GRID_BTN = (By.XPATH, "//button[contains(@class,'gallery')]")

    @allure.step("Обрати фільтр 'Економічний'")
    def select_economic_filter(self):
        self.find_element(self.FILTER_TYPE_DROPDOWN).click()
        self.find_element(self.OPTION_ECONOMIC).click()
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    @allure.step("Перемкнути вигляд на список")
    def switch_to_list(self):
        self.find_element(self.VIEW_LIST_BTN).click()

    @allure.step("Перевірити відображення активного тега фільтра")
    def is_filter_tag_displayed(self):
        try:
            return self.find_element(self.ACTIVE_FILTER_TAG).is_displayed()
        except:
            return False
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGreenCityFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 15)

    def test_filter_by_economic_type(self):

        typ_pod = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'dropdown') and .//mat-label[contains(text(),'Тип події')]]")
        ))
        typ_pod.click()

        drop_menu = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@role='listbox']")
        ))
        self.assertTrue(drop_menu.is_displayed(), 'Випадайка не спрацювала')

        economic = self.wait.until(EC.presence_of_element_located(
            (By.ID, "mat-option-10")
        ))
        economic.click()

        economic_tags = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//span[contains(@class, 'tag-active')]")
        ))

        all_tag_texts = [tag.text.strip() for tag in economic_tags]

        self.assertTrue(all("Economic" in text or "Економічний" in text for text in all_tag_texts),
                        "Помилка")


        # economic = self.wait.until(EC.presence_of_element_located(
        #     (By.ID, "mat-option-10")
        # ))
        # economic.click()

    def tearDown(self):

        self.driver.quit()


import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from statsmodels.graphics.tukeyplot import results


class TestGreenCitySearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_search_by_name(self):

        search_icon = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='search-img']")
        ))
        search_icon.click()

        search_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH,"//input[@placeholder='Search']")
            ))
        search_input.clear()
        search_input.send_keys("S")

        cards = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//mat-card[contains(@class, 'event-list-item')]")
        ))

        # Створюємо список тільки з текстів усіх карток
        all_texts = [card.text for card in cards]
        # Тепер перевіряємо, чи є твоє слово хоча б в одному з цих текстів
        self.assertTrue(any("Some Event" in text for text in all_texts), "в жодній картці не найшло!")

    def tearDown(self):

        self.driver.quit()
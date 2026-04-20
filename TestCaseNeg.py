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

        search_icon = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//span[@class='search-img']")
        ))
        search_icon.click()

        search_input = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Search']")
        ))
        search_input.clear()
        search_input.send_keys("тщьу")

        end_search = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class, 'end-page-txt')]")
        ))
        self.assertTrue(end_search.is_displayed())

    def tearDown(self):

        self.driver.quit()


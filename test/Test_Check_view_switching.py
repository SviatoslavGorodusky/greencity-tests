import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGreenCityViewToggle(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        self.wait = WebDriverWait(self.driver, 10)

    def test_toggle_view_icons(self):
        list_horizon = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class,'list')]")
        ))
        list_horizon.click()

        active_list_horizon = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class, 'list') and contains(@aria-pressed, 'true')]")
        ))
        self.assertTrue(active_list_horizon.is_displayed(), "Вигляд списку не став активним")


        list_vert = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class,'gallery')]")
        ))
        list_vert.click()

        active_list_vert = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class,'gallery') and contains(@aria-pressed, 'true')]")
        ))
        self.assertTrue(active_list_vert.is_displayed(), "Не змінився  по вертикалі")

    def tearDown(self):
        self.driver.quit()

import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv

# Завантажуємо змінні з файлу .env у пам'ять
load_dotenv()

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Замість прямого посилання, беремо його з файлу .env
    # Якщо посилання в файлі не знайдено, відкриється порожня сторінка
    url = os.getenv("BASE_URL")
    driver.get(url)

    yield driver

    driver.quit()
import allure
import pytest
from selenium.webdriver.common.by import By
from src.pages.events_page import EventsPage


@allure.feature("Events Page")  # Головна фіча
class TestEvents:

    @allure.story("Search functionality")
    @allure.title("Negative search: Verify 'No results' message")
    def test_negative_search_message(self, browser):
        events_page = EventsPage(browser)

        with allure.step("Open events page"):
            events_page.open()

        with allure.step("Perform search with non-existing query 'Some'"):
            events_page.header.perform_search("Some")

        with allure.step("Verify that 'No results' title is displayed"):
            expected_text = "Ми не знайшли жодних результатів, що відповідають цьому запиту"
            actual_text = events_page.get_empty_message_text()

            assert expected_text in actual_text, f"Expected '{expected_text}', but got '{actual_text}'"

    @allure.story("Filter functionality")
    @allure.title("Verify all cards are 'Economic' after filtering")
    def test_filter_by_type(self, browser):
        events_page = EventsPage(browser)
        events_page.open()

        with allure.step("Apply 'Economic' filter"):
            events_page.filters.select_economic_filter()

        with allure.step("Verify all displayed cards have 'Економічний' tag"):
                # Метод get_all_cards тепер сам чекає на появу елементів
            cards = events_page.get_all_cards()

            assert len(cards) > 0, "No cards found after filtering!"

            for card in cards:
                    # Використовуємо знайдений на скріншоті локатор всередині кожної картки
                card_type = card.find_element(By.XPATH, ".//span[contains(@class, 'tag-active')]").text

                assert card_type == "ЕКОНОМІЧНИЙ"

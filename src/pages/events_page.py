from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from src.components.header import Header
from src.components.filter_panel import FilterPanel

class EventsPage(BasePage):
    CARD_TYPE_LABEL = (By.XPATH, ".//span[contains(@class, 'tag-active')]")
    EVENT_CARDS = (By.TAG_NAME, "app-events-list-item")
    EMPTY_RESULT_TITLE = (By.XPATH, "//p[contains(text(), 'Ми не знайшли жодних результатів')]")
    EMPTY_RESULT_MSG = (By.XPATH, "//p[contains(@class, 'end-page-txt')]")
    EVENT_CARD_TITLE = (By.XPATH, "//div[contains(@class, 'title-list')]")
    LIST_VIEW_ACTIVE = (By.XPATH, "//button[contains(@class, 'list') and contains(@aria-pressed, 'true')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.filters = FilterPanel(driver)

    def get_first_event_title(self):
        return self.find_element(self.EVENT_CARD_TITLE).text

    def is_empty_message_displayed(self):
        return self.find_element(self.EMPTY_RESULT_MSG).is_displayed()

    def get_empty_message_text(self):
        element = self.find_element(self.EMPTY_RESULT_TITLE)
        return element.text

    def wait_for_cards_to_load(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.EVENT_CARDS))

    def get_all_cards(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.EVENT_CARDS))
            return self.driver.find_elements(*self.EVENT_CARDS)
        except:
            return []
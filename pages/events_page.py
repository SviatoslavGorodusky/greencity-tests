from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EventsPage(BasePage):

    SEARCH_ICON = (By.XPATH, "//span[@class='search-img']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    EMPTY_RESULT_MSG = (By.XPATH, "//p[contains(@class, 'end-page-txt')]")
    EVENT_CARD_TITLE = (By.XPATH, "//div[contains(@class, 'title-list')]")

    FILTER_TYPE_DROPDOWN = (By.XPATH,"//div[contains(@class, 'dropdown') and .//mat-label[contains(text(),'Тип події')]]")
    OPTION_ECONOMIC = (By.XPATH, "//mat-option//span[contains(text(), 'Економічний')]")
    ACTIVE_FILTER_TAG = (By.XPATH, "//span[contains(@class, 'tag-active')]")

    VIEW_LIST_BTN = (By.XPATH, "//button[contains(@class,'list')]")
    VIEW_GRID_BTN = (By.XPATH, "//button[contains(@class,'gallery')]")
    LIST_VIEW_ACTIVE = (By.XPATH, "//button[contains(@class, 'list') and contains(@aria-pressed, 'true')]")
    GRID_VIEW_ACTIVE = (By.XPATH, "//button[contains(@class, 'gallery') and contains(@aria-pressed, 'true')]")

    def open_search(self):
        self.click(self.SEARCH_ICON)

    def enter_search_query(self, text):
        self.type_text(self.SEARCH_INPUT, text)

    def open_filter_type(self):
        self.click(self.FILTER_TYPE_DROPDOWN)

    def select_economic_option(self):
        self.click(self.OPTION_ECONOMIC)

    def click_active_filter_tag(self):
        self.click(self.ACTIVE_FILTER_TAG)

    def switch_to_list_view(self):
        self.click(self.VIEW_LIST_BTN)

    def switch_to_grid_view(self):
        self.click(self.VIEW_GRID_BTN)

    def is_empty_message_displayed(self):
        return self.find_element(self.EMPTY_RESULT_MSG).is_displayed()

    def is_filter_tag_displayed(self):
        return self.find_element(self.ACTIVE_FILTER_TAG).is_displayed()

    def get_first_event_title(self):
        return self.find_element(self.EVENT_CARD_TITLE).text

    def is_list_view_active(self):
        return self.find_element(self.LIST_VIEW_ACTIVE).is_displayed()

    def is_grid_view_active(self):
        return self.find_element(self.GRID_VIEW_ACTIVE).is_displayed()
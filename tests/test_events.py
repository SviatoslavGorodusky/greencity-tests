import pytest
from pages.events_page import EventsPage

# 1. Фільтрація
def test_filter_by_economic_type(browser):
    events_page = EventsPage(browser)
    events_page.open_filter_type()
    events_page.select_economic_option()
    assert events_page.is_filter_tag_displayed(), "Фільтр не активний"
    events_page.click_active_filter_tag()

# 2. Позитивний пошук
def test_search_positive(browser):
    events_page = EventsPage(browser)
    event_name = "Green City"
    events_page.open_search()
    events_page.enter_search_query(event_name)
    actual_title = events_page.get_first_event_title()
    assert event_name.lower() in actual_title.lower(), "Назва не збігається"

# 3. Перемикання вигляду
def test_view_mode_toggle(browser):
    events_page = EventsPage(browser)
    events_page.switch_to_list_view()
    assert events_page.is_list_view_active(), "Список не активний"
    events_page.switch_to_grid_view()
    assert events_page.is_grid_view_active(), "Сітка не активна"

# 4. Негативний пошук
def test_negative_search(browser):
    events_page = EventsPage(browser)
    events_page.open_search()
    events_page.enter_search_query("тщьу")
    assert events_page.is_empty_message_displayed(), "Повідомлення не з'явилося"
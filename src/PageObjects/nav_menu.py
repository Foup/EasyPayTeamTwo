from src.PageObjects.page import Page
from src.locators import HomePage, PathToCounters
from src.PageObjects.counters_page import Counters


class NavMenu(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element(HomePage.nav_menu)

    def open_schedule_page(self):
        pass

    def open_counters_page(self):
        self.click_on_element(PathToCounters.menu_item) \
            .wait_for_element(PathToCounters.panel)
        counter_page = Counters(self.driver)
        return counter_page

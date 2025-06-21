from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results import SearchResultsPage
from pages.cart import Cart


class Application:
    def __init__(self, driver):
        self.base = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results = SearchResultsPage(driver)
        self.cart = Cart(driver)

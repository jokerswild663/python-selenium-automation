from pages.base_page import Page
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results import SearchResultsPage
from pages.cart import Cart
from pages.sign_in import SignIn
from pages.terms_conditions import TermsConditions


class Application:
    def __init__(self, driver):
        self.base = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results = SearchResultsPage(driver)
        self.cart = Cart(driver)
        self.sign_in = SignIn(driver)
        self.terms_conditions = TermsConditions(driver)
        self.help_page = HelpPage(driver)

from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-test*='@web/Search']")
    SEARCH_SUBMIT = (By.CSS_SELECTOR, "button[data-test*='@web/Search/SearchButton']")

    def search_product(self,search_item):
        self.input_text(search_item,*self.SEARCH_INPUT)
        self.click_element(*self.SEARCH_SUBMIT)
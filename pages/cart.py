from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    CART_ICON = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon'] svg")
    CART_EMPTY = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1[class*='styles_ndsHeading']")

    def click_cart(self):
        self.click_element(*self.CART_ICON)

    def verify_cart_empty(self,expected):
        actual=self.find_element(*self.CART_EMPTY).text
        assert actual == expected, f"actual: {actual}, expected: {expected}"
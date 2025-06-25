from pages.base_page import Page
from selenium.webdriver.common.by import By

class Cart(Page):
    CART_ICON = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon'] svg")
    CART_EMPTY = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1[class*='styles_ndsHeading']")
    CART_ICON_FROM_SEARCH = (By.CSS_SELECTOR, "div[style='display: inline-block;'] button[class*='styles_ndsBaseButton']")
    CART_ICON_FROM_PANEL = (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    CART_ITEM = (By.CSS_SELECTOR, "h2[data-test='modal-drawer-heading'] span.h-text-lg")
    CART_ITEMS = (By.CSS_SELECTOR, "div.product-image img")

    def click_cart(self):
        self.click_element(*self.CART_ICON)

    def click_cart_from_search(self):
        self.click_element(*self.CART_ICON_FROM_SEARCH)

    def click_cart_from_panel(self):
        self.click_element(*self.CART_ICON_FROM_PANEL)

    def verify_items_in_cart(self):
        self.verify_elements_found(*self.CART_ITEMS)

    def verify_cart_empty(self,expected):
        actual=self.find_element(*self.CART_EMPTY).text
        assert actual == expected, f"actual: {actual}, expected: {expected}"
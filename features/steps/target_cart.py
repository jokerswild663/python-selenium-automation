from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CART_ICON=(By.CSS_SELECTOR,"div[data-test='@web/CartIcon'] svg")
CART_ICON_FROM_SEARCH=(By.CSS_SELECTOR, "div[style='display: inline-block;'] button[class*='styles_ndsBaseButton']")
CART_ICON_FROM_PANEL=(By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
CART_ITEM=(By.CSS_SELECTOR,"h2[data-test='modal-drawer-heading'] span.h-text-lg")
CART_ITEMS=(By.CSS_SELECTOR, "div.product-image img")

@when("click cart {cart_icon}")
def click_cart(context,cart_icon):
    context.driver.find_element(*CART_ICON).click()


@when("click add to cart from search")
def click_add_to_cart_search(context):
    sleep(10)
    context.driver.find_element(*CART_ICON_FROM_SEARCH).click()
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



@when("click add to cart panel")
def click_add_to_cart_panel(context):
  context.driver.wait.until(
      EC.element_to_be_clickable(CART_ICON_FROM_PANEL)
  ).click()


@then("verify {item} in cart")
def verify_in_cart(context,item):
    products_in_cart=context.driver.find_elements(*CART_ITEMS)
    assert len(products_in_cart) > 0, f"actual length: {len(products_in_cart)}"


@then("verify {object} empty")
def cart_empty(context,object):
    products_in_cart=context.driver.find_elements(*CART_ITEMS)
    assert len(products_in_cart) == 0



from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("click cart {cart_icon}")
def click_cart(context,cart_icon):
    context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/CartIcon'] svg").click()


@when("click add to cart from search")
def click_add_to_cart_search(context):
    context.driver.execute_script("window.scrollTo(0, 1000)")
    context.driver.find_element(By.CSS_SELECTOR, "div[style='display: inline-block;'] button[class*='styles_ndsBaseButton']").click()
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@when("click add to cart panel")
def click_add_to_cart_panel(context):
  context.driver.find_element(By.CSS_SELECTOR, "button[data-test='orderPickupButton']").click()
  sleep(5)


@then("verify {item} in cart")
def verify_in_cart(context,item):
    actual=context.driver.find_element(By.CSS_SELECTOR,"h2[data-test='modal-drawer-heading'] span.h-text-lg").text
    expected="Added to cart"
    assert actual==expected, f"actual: {actual} not equal expected: {expected}"


@then("verify {object} empty")
def cart_empty(context,object):
    products_in_cart=context.driver.find_elements(By.CSS_SELECTOR, "div.product-image img")
    sleep(5)
    assert len(products_in_cart) > 0, "no products in cart"



from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("click cart {cart_icon}")
def click_cart(context,cart_icon):
    context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/CartIcon'] svg").click()


@then("verify {object} empty")
def cart_empty(context,object):
    expected='Your cart is empty'
    actual=context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1[class*='ndsHeading']").text
    sleep(5)
    assert actual==expected, f"actual: '{actual}' does not equal expected: '{expected}'"
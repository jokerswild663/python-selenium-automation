from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@when("click cart {cart_icon}")
def click_cart(context,cart_icon):
    context.app.cart.click_cart()


@when("click add to cart from search")
def click_add_to_cart_search(context):
    sleep(15)
    context.app.cart.click_cart_from_search()



@when("click add to cart panel")
def click_add_to_cart_panel(context):
  context.app.cart.click_cart_from_panel()


@then("verify {item} in cart")
def verify_in_cart(context,item):
    context.app.cart.verify_items_in_cart()


@then("verify {object} empty")
def cart_empty(context,object):
    context.app.cart.verify_cart_empty('Your cart is empty')



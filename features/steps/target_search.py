from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open {url}')
def navigate(context,url):
    context.driver.get(f'https://{url}')


@when("click cart {cart_icon}")
def click_cart(context,cart_icon):
    context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/CartIcon'] svg").click()


@then("verify {object} empty")
def cart_empty(context,object):
    expected='Your cart is empty'
    actual=context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1[class*='ndsHeading']").text
    sleep(5)
    assert actual==expected, f"actual: '{actual}' does not equal expected: '{expected}'"

@when("click account {dropdown}")
def click_account(context,dropdown):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()


@when("click sign in {button}")
def click_sign_in(context,button):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()


@then("verify {page} loaded")
def sign_in_page_loaded(context,page):
    expected='Sign in or create account'
    actual=context.driver.find_element(By.CSS_SELECTOR, "div[tabindex='-1'] h1.h-margin-b-tiny").text
    assert actual==expected, f"actual: '{actual}' does not match expected: '{expected}'"
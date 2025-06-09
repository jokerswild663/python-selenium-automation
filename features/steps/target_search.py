from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open target.com")
def navigate(context):
    context.driver.get("https://target.com")


@when("click cart")
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"div[data-test='@web/CartIcon'] svg").click()


@then("verify cart empty")
def cart_empty(context):
    expected='Your cart is empty'
    actual=context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1[class*='ndsHeading']").text
    sleep(5)
    assert actual==expected, f"actual: '{actual}' does not equal expected: '{expected}'"

@when("click account dropdown")
def click_account(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()


@then("click sign in")
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()


@then("verify sign in page loaded")
def sign_in_page_loaded(context):
    expected='Sign in or create account'
    actual=context.driver.find_element(By.CSS_SELECTOR, "div[tabindex='-1'] h1.h-margin-b-tiny").text
    assert actual==expected, f"actual: '{actual}' does not match expected: '{expected}'"
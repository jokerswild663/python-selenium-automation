from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

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
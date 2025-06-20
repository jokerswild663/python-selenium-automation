from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ACCOUNT_ICON=(By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
ACCOUNT_ICON_PANEL=(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
ACCOUNT_SIGN_IN=(By.CSS_SELECTOR, "div[tabindex='-1'] h1.h-margin-b-tiny")

@when("click account {dropdown}")
def click_account(context,dropdown):
    context.driver.wait.until(EC.element_to_be_clickable(ACCOUNT_ICON)).click()


@when("click sign in {button}")
def click_sign_in(context,button):
    context.driver.wait.until(EC.element_to_be_clickable(ACCOUNT_ICON_PANEL)).click()


@then("verify {page} loaded")
def sign_in_page_loaded(context,page):
    expected='Sign in or create account'
    actual=context.driver.wait.until(EC.visibility_of_element_located(ACCOUNT_SIGN_IN)).text
    assert actual==expected, f"actual: '{actual}' does not match expected: '{expected}'"
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@when("click account {dropdown}")
def click_account(context,dropdown):
    context.app.sign_in.click_sign_in()


@when("click sign in {button}")
def click_sign_in(context,button):
    context.app.sign_in.click_sign_in_panel()

@then("verify {page} loaded")
def sign_in_page_loaded(context,page):
    expected='Sign in or create account'
    context.app.sign_in.verify_sign_in(expected)
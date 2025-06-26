from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@given("Open sign in page for terms and conditions")
def open_sign_in_page(context):
    context.driver.get("https://www.target.com/orders?lnk=acct_nav_my_account")

@when("Store original window")
def store_window(context):
    context.original_window_id=context.app.terms_conditions.current_window()

@when("Click on Target terms and conditions link")
def click_terms_conditions(context):
    context.app.terms_conditions.click_terms_conditions_link()

@when("Switch to the newly opened window")
def switch_new_window(context):
    context.all_windows=context.app.terms_conditions.get_all_windows()
    new_window=context.app.terms_conditions.switch_to_window_by_id(context.all_windows[1])

@then("Verify Terms and Conditions page is opened")
def verify_terms_opened(context):
    context.app.terms_conditions.verify_terms_window_opened(context.all_windows[1])

@then("User can close new window and switch back to original")
def close_terms_window(context):
    context.app.terms_conditions.close_terms_window()
    context.app.terms_conditions.switch_to_original_window(context.original_window_id)
    context.app.terms_conditions.verify_original_window_opened(context.original_window_id)

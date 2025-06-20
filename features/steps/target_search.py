from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT=(By.CSS_SELECTOR,"input[data-test*='@web/Search']")
SEARCH_SUBMIT=(By.CSS_SELECTOR,"button[data-test*='@web/Search/SearchButton']")
SEARCH_RESULT=(By.CSS_SELECTOR,"span.h-text-bs.h-text-grayDark")

@when("target search {entry}")
def target_search(context,entry):
    context.driver.wait.until(EC.visibility_of_element_located(SEARCH_INPUT)).send_keys(entry)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT)).click()

@then("verify search {entry}")
def verify_search(context,entry):
    expected=entry
    actual=context.driver.wait.until(EC.visibility_of_element_located(SEARCH_RESULT)).text
    assert expected in actual, f"expected: '{expected}' does not match actual: '{actual}'"

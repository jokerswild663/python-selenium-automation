from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("target search {entry}")
def target_search(context,entry):
    context.driver.find_element(By.CSS_SELECTOR,"input[data-test*='@web/Search']").send_keys(entry)
    context.driver.find_element(By.CSS_SELECTOR,"button[data-test*='@web/Search/SearchButton']").click()
    sleep(5)

@then("verify search {entry}")
def verify_search(context,entry):
    expected=entry
    actual=context.driver.find_element(By.CSS_SELECTOR,"span.h-text-bs.h-text-grayDark").text
    assert expected in actual, f"expected: '{expected}' does not match actual: '{actual}'"

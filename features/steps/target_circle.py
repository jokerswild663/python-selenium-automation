from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open target circle")
def open_page(context):
  context.driver.get('https://target.com/circle')
  sleep(5)

@then("verify at least 10 benefits")
def verify_benefits_cells(context):
  expected=10
  benefit_cells=context.driver.find_elements(By.CSS_SELECTOR,"div[class*=sc-acea07d2]")
  assert len(benefit_cells)>=expected, f"actualength: {len(benefit_cells)}, expected: {expected}"
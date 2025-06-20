from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BENEFITS_CELLS_CONTAINER=(By.CSS_SELECTOR,"div[data-component='Cells Component Container']")
BENEFITS_CELLS=(By.CSS_SELECTOR,"div[class*=sc-acea07d2]")

@given("open target circle")
def open_page(context):
  context.driver.get('https://target.com/circle')

@then("verify at least 10 benefits")
def verify_benefits_cells(context):
  expected=10
  context.driver.wait.until(
    EC.visibility_of_element_located(BENEFITS_CELLS_CONTAINER)
  )
  benefit_cells=context.driver.find_elements(*BENEFITS_CELLS)

  assert len(benefit_cells)>=expected, f"actualength: {len(benefit_cells)}, expected: {expected}"
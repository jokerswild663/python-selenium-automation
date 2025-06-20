from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import re

COLORS_DIV=(By.CSS_SELECTOR, "div[data-module-type='ProductDetailVariationSelector']")
COLORS=(By.CSS_SELECTOR, "picture img[height='64px'][width='64px']")
SELECTED_COLOR=(By.CSS_SELECTOR, "div[class*='styles_headerWrapper']")

@then("click colors and verify")
def click_and_verify(context):
    expected_colors = ['Medium Wash', 'Khaki', 'Light Blue']
    context.driver.wait.until(EC.visibility_of_element_located(COLORS_DIV))
    colors=context.driver.find_elements(*COLORS)
    sleep(10)  ## popups keep coming up and it screws with clicks

    for color in colors:
        context.driver.wait.until(EC.element_to_be_clickable(color))
        color.click()
        color_text=context.driver.find_element(*SELECTED_COLOR).text
        color_text_formatted=re.sub(r'Color.*\n','', color_text)
        assert str(color_text_formatted) in expected_colors, f"actual: {color_text_formatted} not in expected colors: {expected_colors}"
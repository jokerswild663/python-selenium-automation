from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("open target circle")
def open_page(context):
  context.driver.get('https://target.com/circle')
  sleep(5)
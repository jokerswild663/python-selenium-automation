from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target page {url}')
def navigate(context,url):
    context.driver.get(f'https://{url}')
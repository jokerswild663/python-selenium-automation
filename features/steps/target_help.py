from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when("Browse Help dropdown clicked")
def help_dropdown(context):
    context.url = context.app.help_page.selection()

@then("Verify returns url")
def verify_url(context):
    context.app.help_page.verify_url('Purchases&searchQuery')
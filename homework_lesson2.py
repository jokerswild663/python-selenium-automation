from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

## setup
driver_path=ChromeDriverManager().install()
service=Service(driver_path)
driver=webdriver.Chrome(service=service)
driver.maximize_window()

## Chrome
driver.get('https://target.com')

## execute browser
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()

## finding sign-in button
signin=driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")

# Assert text is correct
expected_signin_text="Sign in or create account"
actual_signin_text=signin.text

assert actual_signin_text == expected_signin_text, f"{actual_signin_text} does not match {expected_signin_text}"

sleep(5)

## cleanup
driver.quit()
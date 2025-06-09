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

sleep(1)

## Chrome
driver.get('https://www.amazon.com')
driver.refresh()
sleep(5)

## haul store link
driver.find_element(By.CSS_SELECTOR,"a.nav-a[href*='/haul/store']")

## Amazon logo
driver.find_element(By.CSS_SELECTOR, "a.nav-logo-link[aria-label='Amazon']")

## Music Dropdown
driver.find_element(By.CSS_SELECTOR, "div a.nav-a[data-csa-c-content-id='nav_cs_music']")
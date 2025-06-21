from selenium.webdriver.common.by import By

class Page:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*locator):
        return self.driver.find_element(*locator)

    def click_element(self,*locator):
        self.driver.find_element(*locator).click()

    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self,*locator,expected_text):
        actual_text=self.driver.find_element(*locator).text
        assert actual_text == expected_text, f"actual: {actual_text}, expected: {expected_text}"

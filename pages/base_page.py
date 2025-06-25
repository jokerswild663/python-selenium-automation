from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*locator):
        # return self.driver.find_element(*locator)
        return self.driver.wait.until(EC.presence_of_element_located(locator))

    def click_element(self,*locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()
        # self.driver.find_element(*locator).click()

    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self,expected_text,locator):
        actual_text=self.driver.wait.until(EC.visibility_of_element_located(locator)).text
        assert actual_text == expected_text, f"actual: {actual_text}, expected: {expected_text}"

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

    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self,expected_text,*locator):
        actual_text=self.driver.wait.until(EC.visibility_of_element_located(locator)).text
        assert actual_text == expected_text, f"actual: {actual_text}, expected: {expected_text}"

    def verify_elements_found(self,*locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))
        elements=self.driver.find_elements(*locator)
        assert len(elements) > 0, f"actual length: {len(elements)}"

    def get_current_window_id(self):
        window = self.driver.current_window_handle
        return window

    def get_all_windows(self):
        windows = self.driver.window_handles
        return windows

    def switch_to_window_by_id(self,window_id):
        self.driver.switch_to.window(window_id)
        return self.driver.current_window_handle

    def verify_windows(self,window_id):
        assert self.get_current_window_id() == window_id, f"{self.get_current_window_id()} != {window_id}"

    def verify_partial_url(self,expected_partial_url):
        assert expected_partial_url in self.driver.current_url, f"{expected_partial_url} != {self.driver.current_url}"

    def close_window(self):
        self.driver.close()
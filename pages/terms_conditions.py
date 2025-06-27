from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TermsConditions(Page):
    TERMS_CONDITIONS_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")

    def current_window(self):
        return self.get_current_window_id()



    def click_terms_conditions_link(self):
        self.click_element(*self.TERMS_CONDITIONS_LINK)


    def switch_to_terms_conditions_window(self,window_id):
        new_window=self.switch_to_window_by_id(window_id)
        return new_window


    def switch_to_original_window(self,window_id):
        original_window=self.switch_to_window_by_id(window_id)
        return original_window

    def verify_terms_window_opened(self,window_id):
        self.verify_windows(window_id)
        self.verify_partial_url('terms-conditions')

    def verify_original_window_opened(self,window_id):
        self.verify_windows(window_id)
        self.verify_partial_url('target.com/login')

    def close_terms_window(self):
        self.close_window()
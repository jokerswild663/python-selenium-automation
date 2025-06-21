from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, "span.h-text-bs.h-text-grayDark")

    def verify_search_result(self,entry):
        expected = entry
        actual = self.driver.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULT)).text
        assert expected in actual, f"expected: '{expected}' does not match actual: '{actual}'"


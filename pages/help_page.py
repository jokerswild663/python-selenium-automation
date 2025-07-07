from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HelpPage(Page):
    HELP_TOPIC = (By.CSS_SELECTOR, "select[name*='viewHelpTopics']")
    SELECT_VALUE = 'Orders & Purchases'

    def selection(self):
        help_select=self.find_element(*self.HELP_TOPIC)
        self.select_dropdown(self.SELECT_VALUE,help_select)
        return self.driver.current_url

    def verify_url(self,url):
        self.verify_partial_url(url)

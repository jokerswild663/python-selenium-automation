from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class SignIn(Page):
    ACCOUNT_ICON = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
    ACCOUNT_ICON_PANEL = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
    ACCOUNT_SIGN_IN = (By.CSS_SELECTOR, "div[tabindex='-1'] h1.h-margin-b-tiny")
    ACCOUNT_USERNAME_FIELD = (By.CSS_SELECTOR, "input[name='username']")
    ACCOUNT_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    ACCOUNT_USERNAME_CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[id='login']")
    ACCOUNT_PASSWORD_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='login'][type='submit']")
    ACCOUNT_PASSWORD_INCORRECT_MESSAGE = (By.CSS_SELECTOR, "span[style*='--error-message']")

    def click_sign_in(self):
        self.click_element(*self.ACCOUNT_ICON)

    def click_sign_in_panel(self):
        # self.driver.find_element(*self.ACCOUNT_ICON_PANEL).click()
        self.click_element(*self.ACCOUNT_ICON_PANEL)

    def verify_sign_in(self,expected):
        # actual=self.driver.find_element(*self.ACCOUNT_SIGN_IN)
        actual=self.verify_text(expected,self.ACCOUNT_SIGN_IN)

    def enter_username(self):
        self.input_text('jokerswild663@gmail.com',*self.ACCOUNT_USERNAME_FIELD)
        self.click_element(*self.ACCOUNT_USERNAME_CONTINUE_BUTTON)

    def enter_wrong_password(self):
        self.input_text('blargg',*self.ACCOUNT_PASSWORD_FIELD)
        self.click_element(*self.ACCOUNT_PASSWORD_SUBMIT_BUTTON)

    def verify_wrong_password(self,expected):
        self.verify_text(expected,self.ACCOUNT_PASSWORD_INCORRECT_MESSAGE)

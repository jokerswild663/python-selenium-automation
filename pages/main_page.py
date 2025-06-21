from pages.base_page import Page

class MainPage(Page):
    def open_main_page(self,url):
        self.driver.get(url)



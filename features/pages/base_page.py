
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_aliexpress_page(self):
        self.driver.get("https://www.aliexpress.com/")

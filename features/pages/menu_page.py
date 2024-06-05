import logging
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class MenuPage(BasePage):

    search_field = (By.ID, 'search-words')
    search_button = (By.XPATH, "//input[contains(@class,'search--submit')]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_product(self, product_name):
        self.close_suscription_popup_if_present()
        search_field = self.driver.find_element(*self.search_field)
        search_field.send_keys(product_name)
        search_button = self.driver.find_element(*self.search_button)
        search_button.click()
        logging.info("Searching results for '{}' product".format(product_name))




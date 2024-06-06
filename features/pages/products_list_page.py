import logging

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from features.pages.menu_page import MenuPage


class ProductsListPage(MenuPage):

    page_button = (By.XPATH, "//li[contains(@class,'comet-pagination-item-{}')]")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_page(self, page_number):
        page_button = self.driver.find_element(self.page_button[0], self.page_button[1].format(page_number))
        for i in range(2):
            try:
                page_button.click()
                logging.info("Redirecting to page '{}'".format(page_number))
            except ElementClickInterceptedException:
                # Click on search button to ensure there is not any element intercepting the page button
                self.click_search_field()




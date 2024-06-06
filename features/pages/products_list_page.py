import logging

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.menu_page import MenuPage


class ProductsListPage(MenuPage):

    page_button = (By.XPATH, "//li[contains(@class,'comet-pagination-item-{}')]")
    products_list_view_as_list = (By.XPATH, "//span[contains(@class,'viewlist')]")
    products_in_list = (By.XPATH, "//div[contains(@class,'card--out-wrapper')]")
    previsualize_button = (By.XPATH, ".//div[" + MenuPage.xpath_lower_text + "='previsualizar']")

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

    def select_product_by_position(self, product_position):
        product_list_view_as_list = self.driver.find_element(*self.products_list_view_as_list)
        product_list_view_as_list.click()
        logging.info("List view selected")
        product_in_list_by_position = self.driver.find_elements(*self.products_in_list)[int(product_position) - 1]
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.previsualize_button))
        previsualize_button = product_in_list_by_position.find_element(*self.previsualize_button)
        previsualize_button.click()
        logging.info("Previsualize button clicked")




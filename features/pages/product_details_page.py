from features.logs_utils import adding_log
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.pages.menu_page import MenuPage


class ProductDetailsPage(MenuPage):

    number_of_items_label = (By.XPATH, "//div[contains(@class,'quantity--info')]//div[contains(" +
                             MenuPage.xpath_lower_text + ",'cliente')] "
                             " | //div[contains(@class,'quantity--info')]//span")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_number_of_items_in_availability_label(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.visibility_of_element_located(self.number_of_items_label))
            number_of_items_text = self.driver.find_element(*self.number_of_items_label).text
            if 'solo' in number_of_items_text.lower():
                number_of_items = number_of_items_text.split(' ')[2]
            else:
                number_of_items = number_of_items_text.split(' ')[0]
            adding_log("There are {} items available to buy".format(number_of_items))
            return number_of_items
        except TimeoutException as ex:
            adding_log(str(ex))
            raise Exception("Number of items is not displayed")



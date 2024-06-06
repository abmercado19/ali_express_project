import logging
from selenium.webdriver.common.by import By


class BasePage:
    xpath_lower_text = "translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
    subscription_popup_close_button = (By.XPATH, "//div[./div[contains("
                                       + xpath_lower_text + ",'notificaciones')]]//following-sibling::img")

    def __init__(self, driver):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.driver = driver

    def open_aliexpress_page(self):
        self.driver.get("https://www.aliexpress.com/")

    def close_suscription_popup_if_present(self):
        try:
            close_button = self.driver.find_element(*self.subscription_popup_close_button)
            close_button.click()
            logging.info("Subscription popup was closed.")
        except:
            logging.info("Subscription popup is not displayed.")



from features.logs_utils import adding_log
from selenium.webdriver.common.by import By


class BasePage:
    xpath_lower_text = "translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')"
    subscription_popup_close_button = (By.XPATH, "//div[./div[contains("
                                       + xpath_lower_text + ",'notificaciones')]]//following-sibling::img")

    def __init__(self, driver):
        self.driver = driver

    def open_aliexpress_page(self):
        self.driver.get("https://www.aliexpress.com/")
        adding_log("Aliexpress page was opened")

    def close_suscription_popup_if_present(self):
        try:
            close_button = self.driver.find_element(*self.subscription_popup_close_button)
            close_button.click()
            adding_log("Subscription popup was closed.")
        except:
            adding_log("Subscription popup is not displayed.")



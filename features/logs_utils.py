import allure
import logging


def adding_log(text):
    logging.info(text)
    with allure.step(text):
        pass
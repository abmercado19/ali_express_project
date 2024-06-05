import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def before_all(context):
    logging.info("Starting test execution")


def before_scenario(context, scenario):
    logging.info("Running Scenario: {}".format(scenario.name))
    driver = webdriver.Chrome()
    context.driver = driver


def after_scenario(context, scenario):
    context.driver.quit()
    logging.info("Finished Scenario: {}".format(scenario.name))

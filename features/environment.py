import os
import logging
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def before_all(context):
    logging.info("Starting test execution")


def before_scenario(context, scenario):
    logging.info("Running Scenario: {}".format(scenario.name))
    driver = webdriver.Chrome()
    context.driver = driver


def before_step(context, step):
    logging.info("Running Step: {}".format(step.name))


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        # Take a screenshot on failure
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_file = os.path.join(screenshot_dir, f"{scenario.name}.png")
        context.driver.save_screenshot(screenshot_file)
        allure.attach.file(screenshot_file, name=scenario.name, attachment_type=AttachmentType.PNG)
        print(f"Screenshot saved to {screenshot_file}")
    context.driver.quit()
    logging.info("Finished Scenario: {}".format(scenario.name))

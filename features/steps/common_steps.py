from behave import *
from features.pages.base_page import BasePage


@given("I open Aliexpress page")
def open_aliexpress_page(context):
    """
    :param context: behave.runner.Context
    """
    base_page = BasePage(context.driver)
    base_page.open_aliexpress_page()

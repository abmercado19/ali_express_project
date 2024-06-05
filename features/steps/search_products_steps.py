from behave import *
from features.pages.menu_page import MenuPage


@when('I search for "{product_name}"')
def search_product_by_name(context, product_name):
    """
    :param context: behave.runner.Context
    :param product_name: str
    """
    menu_page = MenuPage(context.driver)
    menu_page.search_product(product_name)

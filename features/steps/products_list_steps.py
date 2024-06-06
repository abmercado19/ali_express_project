from behave import *

from features.pages.products_list_page import ProductsListPage


@step("I navigate to {page_number}st page")
@step("I navigate to {page_number}nd page")
@step("I navigate to {page_number}rd page")
@step("I navigate to {page_number}th page")
def navigate_to_page(context, page_number):
    """
    :param context: behave.runner.Context
    :param page_number: str
    """
    products_list_page = ProductsListPage(context.driver)
    products_list_page.navigate_to_page(page_number)


@step("I preview the details of the {item_position}st item in the list")
@step("I preview the details of the {item_position}nd item in the list")
@step("I preview the details of the {item_position}rd item in the list")
@step("I preview the details of the {item_position}th item in the list")
def preview_item_in_product_list_by_position(context, item_position):
    """
    :param context: behave.runner.Context
    :param item_position: str
    """
    products_list_page = ProductsListPage(context.driver)
    products_list_page.select_product_by_position(item_position)
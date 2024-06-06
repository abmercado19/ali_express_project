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


@step("I click on the 2nd item in the list")
def step_impl(context):
    """
    :param context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click on the 2nd item in the list')
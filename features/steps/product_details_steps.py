from behave import *
from features.pages.product_details_page import ProductDetailsPage


@then("I see at least {items_quantity} item to buy")
def verify_there_are_available_items(context, items_quantity):
    """
    :param context: behave.runner.Context
    :param items_quantity: str
    """
    product_details_page = ProductDetailsPage(context.driver)
    items_in_availability_label = int(product_details_page.get_product_number_of_items_in_availability_label())
    assert items_in_availability_label >= int(items_quantity), "There is not any item available to buy"

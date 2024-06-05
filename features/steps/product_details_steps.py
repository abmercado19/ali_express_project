from behave import *

use_step_matcher("re")


@then("I see at least 1 item to buy")
def step_impl(context):
    """
    :param context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then I see at least 1 item to buy')
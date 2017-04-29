
from behave import *

from Behave_test2.twentyone import Dealer


@given('a {hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')

@when('the dealer sums the cards')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()

@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total == total)
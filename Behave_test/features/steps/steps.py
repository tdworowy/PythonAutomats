
from behave import *



@given("Add {numbers:d} {result:d}")
def sumP(context,numbers,result):
    ele = numbers.split(',')
    x =int(ele[0])
    y =int(ele[1])
    assert x+y is result




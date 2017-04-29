
from behave import *



@given("Add {numbers} {result}")
def sumP(context,numbers,result):
    ele = numbers.split(',')
    x =int(ele[0])
    y =int(ele[1])
    assert x+y is result




import logging

from Behave.features.steps.steps import SetUp, tearDown

logging.basicConfig(level=logging.INFO, filename="Logs.log")


def before_all(context):
    logging.info("test logging")

def before_scenario(context, scenario):
    logging.info("Test Started")
    SetUp(context)



def after_scenario(context, scenario):
    logging.info("Test Finished")
    tearDown(context)
import logging
import time

from Behave.features.steps.steps import SetUp, tearDown

logging.basicConfig(level=logging.INFO, filename="Logs.log")


def before_all(context):
    timeStump = time.strftime('%Y-%m-%d %H:%M:%S')
    logging.info(timeStump)

def before_feature(context,feature):
    logging.info("Feature name: "+feature.name)

def before_scenario(context, scenario):
    logging.info("Scenario started: " + scenario.name)
    SetUp(context)


def before_step(context, step):
    logging.info("Step: " + step.name)

def after_scenario(context, scenario):
    logging.info("Test Finished")
    tearDown(context)
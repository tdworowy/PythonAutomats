import logging
import time

from Calculator.Behave.features.steps.steps import SetUp, tearDown, takeScreenshot

logging.basicConfig(level=logging.DEBUG, filename="Logs.log")

BEHAVE_DEBUG = True

def before_all(context):
    timeStump = time.strftime('%Y-%m-%d %H:%M:%S')
    context.log = logging
    logging.info(timeStump)

def before_feature(context,feature):
    logging.info("Feature name: "+feature.name)

def before_scenario(context, scenario):
    logging.info("Scenario started: " + scenario.name)
    logging.info("URL: ",context.driver.current_url)
    SetUp(context)


def before_step(context, step):
    logging.info("Step: " + step.name)

def after_scenario(context, scenario):
    logging.info("Test Finished")
    tearDown(context)

def after_step(context, step):
    takeScreenshot(step.name)
    if BEHAVE_DEBUG and step.status == "failed":
        import ipdb
        logging.info(ipdb.post_mortem(step.exc_traceback))

def after_feature(context,feature):
        logging.info("Feature name: "+feature.name)
        logging.info("Skip reason: "+str(feature.skip_reason))
        logging.info("Status: "+feature.status)



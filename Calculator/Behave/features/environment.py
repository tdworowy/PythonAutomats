import logging
import time

from Calculator.Behave.features.steps.steps import setUp, tearDown, takeScreenshot, getURL, createDir
# logging.basicConfig(level=logging.DEBUG, filename="Logs.log")
from Calculator.Behave.screens.screenPath import getScreenPath

# TODO loging for ewery scenario to separated file

BEHAVE_DEBUG = True

# def before_all(context):
#     # context.timeStump = time.strftime('%Y-%m-%d %H:%M:%S')
#     # context.log = logging
#     # logging.info( context.timeStump )

# def before_feature(context,feature):
#     logging.info("Feature name: "+feature.name)

def before_scenario(context, scenario):
    context.timeStump = time.strftime('%Y-%m-%d %H:%M:%S')
    context.screanDirName = getScreenPath()+"\\"+ scenario.name +"_"+ context.timeStump.replace(":","_")
    createDir(context, context.screanDirName)

    logFile = open(context.screanDirName+"\\Log.log",'a+')
    logging.basicConfig(level=logging.DEBUG, filename= logFile.name,filemode='a+')#TODO don't work
    context.log = logging
    logging.info(context.timeStump)

    logging.info("Scenario started: " + scenario.name)
    setUp(context)
    logging.info("URL: "+getURL(context))



def before_step(context, step):
    logging.info("Step: " + step.name)

def after_scenario(context, scenario):
    logging.info("Test Finished")
    tearDown(context)

def after_step(context, step):
    takeScreenshot(context,context.screanDirName+"\\",step.name)
    if BEHAVE_DEBUG and step.status == "failed":
        import ipdb
        logging.info(ipdb.post_mortem(step.exc_traceback))

def after_feature(context,feature):
        logging.info("Feature name: "+feature.name)
        logging.info("Skip reason: "+str(feature.skip_reason))
        logging.info("Status: "+feature.status)



import time

from Calculator.Behave.features.steps.steps import setUp, tearDown, getURL
# logging.basicConfig(level=logging.DEBUG, filename="Logs.log")
from Calculator.Behave.screens.screenPath import getScreenPath
from Utils.utils import log, createDir, takeScreenshot

BEHAVE_DEBUG = True



def before_feature(context,feature):
    context.logFeatureFile = getScreenPath() + "\\Log.txt"
    log("Start Feature : " + feature.name, context.logFeatureFile)


def before_scenario(context, scenario):
    context.timeStump = str(time.strftime('%Y-%m-%d %H:%M:%S'))
    context.screanDirName = getScreenPath()+"\\"+ scenario.name +"_"+ context.timeStump.replace(":","_")
    createDir(context, context.screanDirName)

    context.logFile = context.screanDirName+"\\Log.txt"

    log("Scenario started: " + scenario.name,context.logFile)
    setUp(context)
    log("URL: "+getURL(context),context.logFile)



def before_step(context, step):
    log("Step: " + step.name,context.logFile)

def after_scenario(context, scenario):
    log("Test Finished",context.logFile)
    tearDown(context)

def after_step(context, step):
    takeScreenshot(context,context.screanDirName+"\\",step.name)
    if BEHAVE_DEBUG and step.status == "failed":
        import ipdb
        log("TEST FAIL")
        log(str(ipdb.post_mortem(step.exc_traceback)),context.logFile)

def after_feature(context,feature):

    log("Feature Finished: "+feature.name,context.logFeatureFile)
    log("Skip reason: "+str(feature.skip_reason),context.logFeatureFile)
    log("Status: "+feature.status,context.logFeatureFile)



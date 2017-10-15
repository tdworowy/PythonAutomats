import time

from Blog_Tests.Pages.base_page import tear_down
from Blog_Tests.screens.screenPath import get_screen_path
from Utils.utils import log, create_dir, take_screenshot

BEHAVE_DEBUG = True


def before_feature(context, feature):
    context.logFeatureFile = get_screen_path() + "\\Log.txt"
    log("Start Feature : " + feature.name, context.logFeatureFile)


def before_scenario(context, scenario):
    context.time_stump = str(time.strftime('%Y-%m-%d %H:%M:%S'))
    context.screen_dir_name = get_screen_path() + "\\" + scenario.name + "_" + context.time_stump.replace(":", "_")
    create_dir(context, context.screen_dir_name)
    context.log_file = context.screen_dir_name + "\\{%s}Log{%s}.txt" % (scenario.name,context.time_stump)
    log("Scenario started: " + scenario.name, context.log_file)


def before_step(context, step):
    log("Step: " + step.name, context.logFile)


def after_scenario(context, scenario):
    log("Test Finished", context.logFile)
    tear_down(context)


def after_step(context, step):
    take_screenshot(context, context.screanDirName + "\\", step.name)
    if BEHAVE_DEBUG and step.status == "failed":
        import ipdb
        log("TEST FAIL")
        log(str(ipdb.post_mortem(step.exc_traceback)), context.logFile)


def after_feature(context, feature):
    log("Feature Finished: " + feature.name, context.logFeatureFile)
    log("Skip reason: " + str(feature.skip_reason), context.logFeatureFile)
    log("Status: " + feature.status, context.logFeatureFile)

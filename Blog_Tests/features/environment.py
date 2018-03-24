import time

from Blog_Tests.Pages.base_page import tear_down
from Blog_Tests.screens.screenPath import get_screen_path
from Utils.utils import log, create_dir, take_screenshot

BEHAVE_DEBUG = True


def before_feature(context, feature):
    context.log_feature_file = get_screen_path() + "\\%s_Log.txt" % feature.name
    log("Start Feature : " + feature.name, context.log_feature_file)


def before_scenario(context, scenario):
    context.scenario_name = scenario.name.replace(" ", "_")
    context.time_stump = str(time.strftime('%Y-%m-%d_%H_%M_%S'))
    context.screen_dir_name = get_screen_path() + "\\" + context.scenario_name + "_" + context.time_stump
    create_dir(context, context.screen_dir_name)
    context.log_file = context.screen_dir_name + "\\%s_Log_%s.txt" % (context.scenario_name, context.time_stump)
    log("Scenario started: " + scenario.name, context.log_file)


def before_step(context, step):
    log("Step: " + step.name, context.log_file)


def after_scenario(context, scenario):
    log("Test Finished: " + context.scenario_name, context.log_file)
    log("Status: " + str(scenario.status), context.log_file)
    tear_down(context)


def after_step(context, step):
    take_screenshot(context, context.screen_dir_name + "\\", "%s_%s" % (context.scenario_name, step.name))
    log("Status: " + str(step.status), context.log_file)
    if BEHAVE_DEBUG and str(step.status) == "failed":
        import ipdb
        log("TEST FAIL", context.log_file)
        log(str(ipdb.post_mortem(step.exc_traceback)), context.log_file)


def after_feature(context, feature):
    log("Feature Finished: " + feature.name, context.log_feature_file)
    log("Skip reason: " + str(feature.skip_reason), context.log_feature_file)
    log("Status: " + str(feature.status), context.log_feature_file)

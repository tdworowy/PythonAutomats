import time

from Blog_Tests.Pages.base_page import tear_down
from Blog_Tests.screens.screenPath import get_screen_path
from Utils.utils import log, create_dir, take_screenshot

BEHAVE_DEBUG = True


def before_feature(context, feature):
    context.log_feature_file = get_screen_path() + "\\%s_Log.log" % feature.name
    log(context.log_feature_file).info("Start Feature: " + feature.name)


def before_scenario(context, scenario):
    context.scenario_name = scenario.name.replace(" ", "_")
    context.time_stump = str(time.strftime('%Y-%m-%d_%H_%M_%S'))
    context.screen_dir_name = get_screen_path() + "\\" + context.scenario_name + "_" + context.time_stump
    create_dir(context, context.screen_dir_name)
    context.log_file = context.screen_dir_name + "\\%s_Log_%s.log" % (context.scenario_name, context.time_stump)
    log(context.log_file).info("Scenario started: " + scenario.name)


def before_step(context, step):
    log(context.log_file).info("Step: " + step.name)


def after_scenario(context, scenario):
    log(context.log_file).info("Test Finished: " + context.scenario_name)
    log(context.log_file).info("Scenario status: " + str(scenario.status))
    tear_down(context)


def after_step(context, step):
    take_screenshot(context, context.screen_dir_name + "\\", "%s_%s" % (context.scenario_name, step.name))
    log(context.log_file).info("Step status: " + str(step.status))
    if BEHAVE_DEBUG and str(step.status) == "Status.failed":
        import ipdb
        log(context.log_file).error("TEST FAIL")
        log(context.log_file).error(str(ipdb.post_mortem(step.exc_traceback)))
        log(context.log_file).error(context.get_log('browser'),)
        log(context.log_file).error(context.get_log('driver'))


def after_feature(context, feature):
    log(context.log_feature_file)
    log(context.log_feature_file).info("Feature Finished: " + feature.name)
    log(context.log_feature_file).info("Feature status: " + str(feature.status))

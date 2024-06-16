import time

from Calculator.Behave.features.steps.steps import set_up, tear_down, get_url

# logging.basicConfig(level=logging.DEBUG, filename="Logs.log")
from Calculator.Behave.screens.screenPath import get_screen_path
from Utils.utils import create_dir, take_screenshot, MyLogging

BEHAVE_DEBUG = True


def before_feature(context, feature):
    context.mylogging = MyLogging()
    context.logFeatureFile = get_screen_path() + "\\Log.txt"
    context.mylogging.log(context.logFeatureFile).info(
        "Start Feature : " + feature.name
    )


def before_scenario(context, scenario):
    context.timeStump = str(time.strftime("%Y-%m-%d %H:%M:%S"))
    context.screanDirName = (
        get_screen_path()
        + "\\"
        + scenario.name
        + "_"
        + context.timeStump.replace(":", "_")
    )
    create_dir(context, context.screanDirName)

    context.logFile = context.screanDirName + "\\Log.txt"

    context.mylogging.log(context.logFile).info("Scenario started: " + scenario.name)
    set_up(context)
    context.mylogging.log(context.logFile).info("URL: " + get_url(context))


def before_step(context, step):
    context.mylogging.log(context.logFile).info("Step: " + step.name)


def after_scenario(context, scenario):
    context.mylogging.log(context.logFile).info("Test Finished")
    tear_down(context)


def after_step(context, step):
    take_screenshot(context, context.screanDirName + "\\", step.name)
    if BEHAVE_DEBUG and step.status == "failed":
        import ipdb

        context.mylogging.log(context.logFile).error("TEST FAIL")
        context.mylogging.log(context.logFile).error(
            str(ipdb.post_mortem(step.exc_traceback))
        )


def after_feature(context, feature):
    context.mylogging.log(context.logFeatureFile).info(
        "Feature Finished: " + feature.name
    )
    context.mylogging.log(context.logFeatureFile).info(
        "Skip reason: " + str(feature.skip_reason)
    )
    context.mylogging.log(context.logFeatureFile).info("Status: " + feature.status)

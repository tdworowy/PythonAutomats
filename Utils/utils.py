import os
import time

def log (text,path =os.path.dirname(os.path.abspath(__file__))+"\\" "log.txt"):
    try:
        text = str(text)
        timeStump = time.strftime('%Y-%m-%d %H:%M:%S')
        log = timeStump+" "+text +"\n"
        print(log)
        print(path)
        with open( path, "a+") as logFile:
            logFile.write(log)
    except Exception as ex:
        print("ERROR while logging")
        print(str(ex))
        raise ex


def logResult(TestName,Result):
        message = "Name: {x} Result {y}".format(x=TestName, y=Result)
        print(message)
        log(message,"TestsResultLog.txt")


def createDir(context,name):
    if not os.path.exists(name):
        os.makedirs(name)

def takeScreenshot(context,path,file):

    context.driver.save_screenshot(path+file.replace(' ','_')+'.png')
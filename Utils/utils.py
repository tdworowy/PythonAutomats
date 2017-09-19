import calendar
import datetime
import os
import time
from datetime import date
historyPath = "D:\Google_drive\Songs\History"

def log (text,path = os.path.dirname(os.path.abspath(__file__))+"\\log.txt"):
    try:
        text = str(text)
        timeStump = time.strftime('%Y-%m-%d %H:%M:%S')
        log = timeStump+" "+text +"\n"
        print(log)
        print(path)
        with open( path, "a") as logFile:
            logFile.write(log)
    except Exception as ex:
        print("ERROR while logging")
        print(str(ex))
        # raise RuntimeError


def saveHistory (text,file):
    log(text,historyPath+file)


def logResult(TestName,Result):
        message = "Name: {x} Result {y}".format(x=TestName, y=Result)
        print(message)
        log(message,"TestsResultLog.txt")


def createDir(context,name):
    if not os.path.exists(name):
        os.makedirs(name)

def takeScreenshot(context,path,file):
    context.driver.save_screenshot(path+file.replace(' ','_')+'.png')

def takeScreenshot_(driver,path,file):
    driver.save_screenshot(path+file.replace(' ','_')+'.png')


def mesageByTime():
        now = datetime.datetime.now()
        dateToday = date.today()
        log("Today is: "+str(calendar.day_name[dateToday.weekday()])+" "+str(date.today()))
        return "Song for "+str(calendar.day_name[dateToday.weekday()])+" "+str(date.today()) + " [AUTO] "


def characters(frm,to):
    return ','.join([chr(x) for x in range(frm,to)]) #max 1114111



def createFileIfNotExist(path):
    if not os.path.isfile(path):
        open(path, 'w').close()

def writeToFileNoDuplicates(path,elements):
    with (open(path,'a')) as f1,(open(path,'r')) as f2:
        for ele in elements:
            inFile = [line.strip() for line in f2.readlines()]
            # print("if %s not in %s " %(ele,list))
            if ele not in inFile:
                f1.write(ele + '\n')
            f2.seek(0)


def getMilis():
    return int(round(time.time() * 1000))
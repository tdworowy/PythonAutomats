import os
import time

def log (text,file = "log.txt"):
    timeStumo = time.strftime('%Y-%m-%d %H:%M:%S')
    log = timeStumo+" "+text +"\n"
    print(log)
    path = os.path.dirname(os.path.abspath(__file__))+"\\"+file
    print(path)
    with open( path, "a+") as logFile:
        logFile.write(log)


def logResult(TestName,Result):
        message = "Name: {x} Result {y}".format(x=TestName, y=Result)
        print(message)
        log(message,"TestsResultLog.txt")
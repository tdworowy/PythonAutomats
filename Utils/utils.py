import os
import time

def log (text):
    timeStumo = time.strftime('%Y-%m-%d %H:%M:%S')
    log = timeStumo+" "+text +"\n"
    print(log)
    path = os.path.dirname(os.path.abspath(__file__))+"\\log.txt"
    with open( path, "a+") as logFile:
        logFile.write(log)

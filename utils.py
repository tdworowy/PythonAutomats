import time

def log (text):
    timeStumo = time.strftime('%Y-%m-%d %H:%M:%S')
    log = timeStumo+" "+text +"/n"
    print(log)
    with open("log.txt", "a+") as logFile:
        logFile.write(log)
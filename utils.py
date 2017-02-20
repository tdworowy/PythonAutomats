import datetime

def log (text):
    time = '{%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    log = time+" "+text
    print(log)
    with open("log.txt", "a") as myfile:
        myfile.write(log)
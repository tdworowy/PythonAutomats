import sys
import time

from Facebook.facebookAPI import FaceBookMessageBot
from Utils.utils import create_file_if_not_exist


class faceThreadMonitor:
    def __init__(self,email,passw,path):
         self.faceBot = FaceBookMessageBot()
         self.faceBot.login(email, passw)
         self.path = path



    def monitorThreads(self,phraze,threadIDs):
        for thread in threadIDs:
           for massage in self.faceBot.get_messages(thread):
              if str(massage.text) == phraze:
                   path = self.path + thread + ".txt"
                   create_file_if_not_exist(path)
                   with open(path, 'r+') as f:
                        msg = str((massage.text,massage.timestamp))
                        line_found = any(msg in line for line in f)
                        if not line_found:
                            f.write(msg+"\n")
                            f.flush()

    def setThreadIDes(self,threadIDs):
        self.threadIDs = threadIDs



def startMonitor(phraze,faceThreadMonitorList):
        while (1):
            for ftm in faceThreadMonitorList:
                ftm.monitorThreads(phraze, ftm.threadIDs)
                time.sleep(60)

if __name__ == '__main__':
    # THREADIDs = ['1252344071467839','100000471818643']
    THREADIDs1 = ['1252344071467839'] #group
    THREADIDs2 = ['100000471818643'] #user

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]
    path1 = 'D:\Google_drive\QueesGroup\\'
    path2 = 'D:\Google_drive\QueesUser\\'

    fm1 = faceThreadMonitor(user,passw,path1)
    fm1.setThreadIDes(THREADIDs1)

    fm2 = faceThreadMonitor(user, passw, path2)
    fm2.setThreadIDes(THREADIDs2)

    startMonitor("[SONG]",[fm1,fm2])

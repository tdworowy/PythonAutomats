import time

from Facebook.facebookAPI import FaceBookMessageBot
from Utils.utils import checkIfFileExist


class faceThreadMonitor:
    def __init__(self,email,passw,path):
         self.faceBot = FaceBookMessageBot()
         self.faceBot.logIn(email,passw)
         self.path = path




    def monitorThreads(self,phraze,threadIDs):
        for thread in threadIDs:
           for massage in self.faceBot.getMessages(thread):
              if str(massage.text) == phraze:
                   path = self.path + thread + ".txt"
                   checkIfFileExist(path)

                   with open(path, 'r+') as f:
                        msg = str((massage.text,massage.timestamp))
                        line_found = any(msg in line for line in f)
                        print(line_found)
                        if not line_found:
                            f.write(msg+"\n")
                            f.flush()

    def startMonitor(self,phraze,threadIDs):
        while (1):
            self.monitorThreads(phraze, threadIDs)
            time.sleep(30)


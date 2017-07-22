import os
import random
import sys
import time
from os import listdir
from os.path import isfile, join

from Facebook.songOfTheDay_facebookMessage import songOfTheDayFace
from Utils.Songs_.Songs import getFilePath
from Utils.utils import createFileIfNotExist, log, saveHistory
from Youtube.YoutubeBot import getYoutubeURL
from fbchat import ThreadType


def checkQuess(path):
     files = [f for f in listdir(path) if isfile(join(path, f))]
     ids = []
     for file in files:
         fileName = os.path.splitext(file)[0]
         checked = path+"checked\\"+fileName + "_checked.txt"
         createFileIfNotExist(checked)
         f2 = open(checked,'r+')
         with open(path+"\\"+file,'r') as f :
             for line in f.readlines():
                 line_found = any(line in line2 for line2 in f2)
                 if not line_found:
                     print(fileName)
                     ids.append(fileName)
                     f2.write(line+'\n')
     return ids


def main(song,THREADID, threadType):

        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")
        ran = random.randrange(len(songsList))
        songTitle =songsList[ran]
        log(songTitle)
        saveHistory(songTitle, "FacebookMessage.txt")
        song.setUp()
        url = getYoutubeURL(song.driver,songTitle.strip())
        song.sentSong([url],THREADID,"SONG ON DEMAND",threadType)
        song.tearDown()

def  thread(song,path,threadType):
        threads = checkQuess(path)
        for thred in threads:
                main(song,thred,threadType)


if __name__ == '__main__':
    path1 = 'D:\Google_drive\QueesGroup\\'
    path2 = 'D:\Google_drive\QueesUser\\'

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]

    song = songOfTheDayFace()
    song.loginFB(user, passw)
    while 1:

        thread(song,path1,ThreadType.GROUP)
        thread(song,path2, ThreadType.USER)
        time.sleep(60)

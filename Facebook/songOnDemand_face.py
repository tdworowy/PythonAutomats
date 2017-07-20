import os
import random
import sys
import time
from os import listdir
from os.path import isfile, join

from Facebook.songOfTheDay_facebookMessage import songOfTheDayFace
from Utils.Songs_.Songs import getFilePath
from Utils.decorators import logExeption
from Utils.utils import createFileIfNotExist, log, saveHistory
from Youtube.YoutubeBot import getYoutubeURL


def checkQuess(path):
     files = [f for f in listdir(path) if isfile(join(path, f))]
     ids = []
     for file in files:
         checked = file + "_checked.txt"
         createFileIfNotExist(checked)
         f2 = open(checked,'r+')
         with open(path+"\\"+file,'r') as f :
             for line in f.read():
                 line_found = any(line in line2 for line2 in f2)
                 if not line_found:
                     ids.append(os.path.splitext(os.path.abspath(f.name))[0])
                     f2.write(line+'\n')
     return ids


@logExeption
def main(login, password,THREADID):
        song = songOfTheDayFace()
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")
        ran = random.randrange(len(songsList))
        songTitle =songsList[ran]
        log(songTitle)
        saveHistory(songTitle, "FacebookMessage.txt")
        url = getYoutubeURL(song.driver,songTitle.strip())
        song.sentSong(login,password, [url],THREADID,"SONG ON DEMAND")
        song.tearDown()


if __name__ == '__main__':
    path = 'D:\Google_drive\Quees\\'

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]

    while 1:
        threads = checkQuess(path)
        for thred in threads:
            main(user,passw,thred)
        time.sleep(60)
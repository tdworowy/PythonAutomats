import os
import random
import sys
import time
from os import listdir
from os.path import isfile, join

from Facebook.songOfTheDay_facebookMessage import SongOfTheDayFace
from Utils.Songs_.Songs import get_file_path
from Utils.utils import create_file_if_not_exist, log, save_history
from Youtube.Youtube_Bot import get_youtube_URL
from fbchat import ThreadType


def checkQuess(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    ids = []
    for file in files:
        fileName = os.path.splitext(file)[0]
        checked = path + "checked\\" + fileName + "_checked.txt"
        create_file_if_not_exist(checked)
        f2 = open(checked, 'r+')
        with open(path + "\\" + file, 'r') as f:
            for line in f.readlines():
                line_found = any(line in line2 for line2 in f2)
                if not line_found:
                    print(fileName)
                    ids.append(fileName)
                    f2.write(line + '\n')
    return ids


def main(song, THREADID, threadType):
    f = open(get_file_path(), 'r')
    log("Get random song")
    songsList = f.read()
    songsList = songsList.split("\n")
    ran = random.randrange(len(songsList))
    songTitle = songsList[ran]
    log(songTitle)
    save_history(songTitle, "FacebookMessage.txt")
    song.set_up()
    url = get_youtube_URL(song.driver, songTitle.strip())
    song.sent_song([url], THREADID, "SONG ON DEMAND", threadType)
    song.tear_down()


def thread(song, path, threadType):
    threads = checkQuess(path)
    for thred in threads:
        main(song, thred, threadType)


if __name__ == '__main__':
    path1 = 'D:\Google_drive\QueesGroup\\'
    path2 = 'D:\Google_drive\QueesUser\\'

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]

    song = SongOfTheDayFace()
    song.login_FB(user, passw)

    while 1:
        thread(song, path1, ThreadType.GROUP)
        thread(song, path2, ThreadType.USER)
        time.sleep(60)

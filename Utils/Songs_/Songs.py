from datetime import date

import requests
from bs4 import BeautifulSoup

from Utils.utils import log

# filePath = os.path.dirname(os.path.abspath(__file__))+'\\file.txt'
filePath = "D:\Google_drive\Songs\songsList.txt"
lastUpdated = "D:\Google_drive\Songs\LastUpdated.txt"

def getFilePath():
    return filePath

def getTitels(count,url):
    log("Get songs from last fm --- START")
    for i in range(count):
        response = requests.get(url + str(i)).text
        soup = BeautifulSoup(response,"html.parser")
        titles = soup.find_all("a", class_="link-block-target")
        titles = str(titles)
        titles = titles.split(">")
        clrTitels = [title.encode("utf-8").decode('ascii','ignore') for title in titles]
    log("Get songs from last fm --- DONE")
    return clrTitels

def clearTitels(titles):
    cleanTitels = []
    for text in titles:
        try:
            # print(text)
            if "—" in text:
                i = text.index("title=\"") + 7
                temp = text[i:-1].replace("—", "-")
                cleanTitels.append(temp+"\n")

        except Exception as ex:
            log(ex)
            continue
    return cleanTitels


def getSongs():
            log("Generate songs list")
            f = open(filePath, 'w')
            count = 0
            titles =clearTitels(getTitels(659,'http://www.last.fm/pl/user/TotaledThomas/library/tracks?page='))
                #print(titles)
            for text in titles:
                try:
                     log(text)
                     count +=1
                     print(text, file=f)
                except Exception as ex:
                     log(str(ex))
                     continue
            log("Songs count: ",count)
            f.close()


def updateSongs():
    dateToday = date.today()
    log("Update songs list")
    f1 = open(filePath)
    f2 = open(filePath, 'a')
    with (open(lastUpdated, 'r')) as f3:
        if f3.readline() == str(dateToday) :
            log("List already updated")
            return 0
    log("Files opened Correctly")
    oldTitels = [line for line in f1.readlines()]
    # newTitles = clearTitels(getTitels(10,"http://www.last.fm/pl/user/TotaledThomas/library?date_preset=LAST_7_DAYS&page="))
    newTitles = clearTitels( getTitels(60, "http://www.last.fm/pl/user/TotaledThomas/library?date_preset=LAST_30_DAYSS&page="))
    log("New titles: "+str(newTitles))
    for title in newTitles:
          try:
              if title not in oldTitels:
                  f2.write(title)
                  f2.flush()
          except Exception as ex:
                  log("Error while updating song list")
                  log(str(ex))
                  continue
    f2.flush()
    f2.close()
    log("Song List updated correctly")
    open(lastUpdated, 'w').write(str(dateToday))


if __name__ == '__main__':
    log("__main__")
    updateSongs()

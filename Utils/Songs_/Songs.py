from datetime import date

import requests
from bs4 import BeautifulSoup

from Utils.utils import log

# filePath = os.path.dirname(os.path.abspath(__file__))+'\\file.txt'
filePath = "D:\Google_drive\Songs\songsList.txt"
lastUpdated = "D:\Google_drive\Songs\LastUpdated.txt"
PAGES = 706
#
# LAST_7_DAYS
# LAST_30_DAYS
# LAST_90_DAYS
# LAST_180_DAYS
# LAST_365_DAYS
# ALL

def getFilePath():
    return filePath

def getTitels(count,url):
    log("Get songs from last fm --- START")
    clrTitels = []
    for i in range(1,count):
        log("Get songs from page %s" % i)
        response = requests.get(url + str(i)).text
        soup = BeautifulSoup(response,"html.parser")
        titles = soup.find_all("a", class_="link-block-target")
        titles = str(titles)
        titles = titles.split(">")
        newTitles = [title.encode("utf-8").decode('ascii','ignore') for title in titles]
        # print(newTitles)
        clrTitels.extend(newTitles)
        log("Get songs from page %s --- DONE" % i)
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
            log('EXEPTION in cleanTitels')
            log(ex)
            continue
    return cleanTitels


def getSongs():
            log("Generate songs list")
            log("Clear existing or create new file")
            open(filePath, 'w').close()
            f = open(filePath, 'a')
            count = 0
            titles =clearTitels(getTitels(PAGES,'https://www.last.fm/pl/user/TotaledThomas/library/tracks?page='))
            print("Songs found: %s" % str(len(titles)))
                #print(titles)
            for text in titles:
                try:
                     count +=1
                     f.write(text)
                     f.flush()
                except Exception as ex:
                     log("EXEPTION while generating songs list")
                     log(str(ex))
                     continue
            log("Songs count: %s" % str(count))
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
    newTitles = clearTitels( getTitels(60, "https://www.last.fm/pl/user/TotaledThomas/library?date_preset=LAST_30_DAYSS&page="))
    log("New titles: "+str(newTitles))
    for title in newTitles:
          try:
              if title not in oldTitels:
                  f2.write(title)
                  f2.flush()
          except Exception as ex:
                  log("Error while updating songs list")
                  log(str(ex))
                  continue
    f2.flush()
    f2.close()
    log("Song List updated correctly")
    open(lastUpdated, 'w').write(str(dateToday))


if __name__ == '__main__':
     getSongs()

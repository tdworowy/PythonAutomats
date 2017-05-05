import os

import requests
from bs4 import BeautifulSoup

from Utils.utils import log

filePath = os.path.dirname(os.path.abspath(__file__))+'\\file.txt'

def getTitels(count,url):
    log("get songs from last fm")
    for i in range(count):
        # response = requests.get('http://www.last.fm/pl/user/TotaledThomas/loved?page='+str(i)).text
        response = requests.get(url + str(i)).text
        soup = BeautifulSoup(response,"html.parser")
        titles = soup.find_all("a", class_="link-block-target")
        titles = str(titles).split(">")
    return titles

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
            print(ex)
            continue
    return cleanTitels


def getSongs():
            log("Generate songs list")
            f= open(filePath, 'w')
            count = 0
            titles =clearTitels(getTitels(659,'http://www.last.fm/pl/user/TotaledThomas/library/tracks?page='))
                #print(titles)
            for text in titles:
                try:
                    print(text)
                    count +=1
                    print(text, file=f)
                except Exception as ex:
                        print(str(ex))
                        continue
            print("Songs count: ",count)
            f.close()


def updateSongs():
    log("Update songs list")
    f1 = open(filePath)
    f2 = open(filePath, 'a')
    oldTitels = [line for line in f1.readlines()]
    newTitles = clearTitels(getTitels(10,"http://www.last.fm/pl/user/TotaledThomas/library?date_preset=LAST_7_DAYS&page="))
    for title in newTitles:
          try:
              if title not in oldTitels:
                  print(title)
                  f2.write(title)
                  f2.flush()
          except Exception as ex:
                  print(str(ex))
                  continue



if __name__ == '__main__':
    updateSongs()

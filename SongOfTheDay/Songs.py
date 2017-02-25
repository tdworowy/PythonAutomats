import requests
from bs4 import BeautifulSoup

from Utils.utils import log


def getTitels(count,url):
    log("get songs from last fm")
    for i in range(count):
        # response = requests.get('http://www.last.fm/pl/user/TotaledThomas/loved?page='+str(i)).text
        response = requests.get(url + str(i)).text
        soup = BeautifulSoup(response)
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
                cleanTitels.append(temp)

        except Exception as ex:
            print(ex)
            continue
    return cleanTitels


def getSongs():
            log("Generate songs list")
            f= open('file.txt', 'w')
            count = 0
            titles =clearTitels(getTitels(659,'http://www.last.fm/pl/user/TotaledThomas/library/tracks?page='))
                #print(titles)
            for text in titles:
                try:
                    print(text)
                    count +=1
                    print(text+"\n", file=f)
                except Exception as ex:
                        print(ex)
                        continue
            print("Songs count: ",count)
            f.close()


def updateSongs():
    log("Update songs list")
    f = open('file.txt', 'a+')
    oldTitels = [line.split('\n') for line in f.readlines()]
    newTitles = clearTitels(getTitels(5,"https://www.last.fm/pl/user/TotaledThomas/library?page="))
    for title in newTitles:
            if title not in oldTitels:
                f.write(title+"\n")

    f.flush()


#getSongs()

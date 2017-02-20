import requests
from bs4 import BeautifulSoup


def getSongs():
            print("Generate songs list")
            f= open('file.txt', 'w')
            count = 0
            for i in range(658):
               # response = requests.get('http://www.last.fm/pl/user/TotaledThomas/loved?page='+str(i)).text
                response = requests.get('http://www.last.fm/pl/user/TotaledThomas/library/tracks?page='+str(i)).text
                soup = BeautifulSoup(response)
                titles = soup.find_all("a", class_="link-block-target")
                titles = str(titles).split(">")
                #print(titles)
                for text in titles:
                    try:
                    #print(text)
                        if "—" in text:
                           i = text.index("title=\"")+7
                           temp = text[i:-1].replace("—","-")         
                           print(temp)
                           count +=1
                           print(temp, file=f)
                    except Exception as ex:
                        print(ex)
                        continue
            print("Songs count: ",count)
            f.close()

getSongs()

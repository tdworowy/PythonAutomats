from datetime import date

import requests
from bs4 import BeautifulSoup

from Utils.utils import log

FILE_PATH = "D:\Google_drive\Songs\songsList.txt"
LAST_UPDATED = "D:\Google_drive\Songs\LastUpdated.txt"


# PAGES = 2
# LAST_7_DAYS
# LAST_30_DAYS
# LAST_90_DAYS
# LAST_180_DAYS
# LAST_365_DAYS
# ALL

def get_pages_count(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    pagination_list = soup.find('ul', class_="pagination-list")
    pages = pagination_list.find_all('a')
    return max([page.text for page in pages[:-1]])


def get_titles(url):
    log("Get songs from %s" % url)
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    titles = soup.find_all("a", class_="link-block-target")
    titles = str(titles)
    titles = titles.split(">")
    return clear_titles(titles)


def clear_titles(titles):
    clean_titles = []
    for text in titles:
        try:
            # print(text)
            if "—" in text:
                i = text.index("title=\"") + 7
                temp = text[i:-1].replace("—", "-")
                clean_titles.append(temp + "\n")

        except Exception as ex:
            log('EXCEPTION in clean_titles')
            log(ex)
            continue
    return clean_titles


def get_songs(user='TotaledThomas'):
    log("Generate songs list")
    log("Clear existing or create new file")
    open(FILE_PATH, 'w').close()
    url = 'https://www.last.fm/pl/user/%s/library/tracks' % user
    pages_count = get_pages_count(url)
    titles = map(get_titles,[url+'?page= %s' % str(i) for i in range(1, pages_count+1)])
    to_file(titles)


def to_file(titles):
    with open(FILE_PATH, 'a') as f, open('songs.txt', 'a') as f2:
        for text in titles:
            try:
                f.write(text)
                f.flush()
                f2.write(text)
                f2.flush()
            except Exception as ex:
                log("EXCEPTION while generating songs list")
                log(str(ex))
                continue


def update_songs(user='TotaledThomas', pages_to_check=60):
    date_today = date.today()
    log("Update songs list")
    with (open(LAST_UPDATED, 'r')) as f3:
        if f3.readline() == str(date_today):
            log("List already updated")
            return 0
    log("Files opened Correctly")
    with open(FILE_PATH) as f1:
        old_titles = [line for line in f1.readlines()]
    url = "https://www.last.fm/pl/user/%s/library?date_preset=LAST_30_DAYSS" % user
    new_titles = map(get_titles,[url+"&page=%s" % str(i) for i in range(1, pages_to_check+1)])
    titles_to_update = [title for title in new_titles if title not in old_titles]
    with open(FILE_PATH, 'a') as f2:
        for title in titles_to_update:
                try:
                    f2.write(title)
                    f2.flush()
                except Exception as ex:
                    log("Error while updating songs list")
                    log(str(ex))
                    continue
    log("Song List updated correctly")
    open(LAST_UPDATED, 'w').write(str(date_today))


if __name__ == '__main__':
   get_songs()


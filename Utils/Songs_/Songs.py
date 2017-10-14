from datetime import date

import requests
from Utils.utils import log
from bs4 import BeautifulSoup

# filePath = os.path.dirname(os.path.abspath(__file__))+'\\file.txt'
FILE_PATH = "D:\Google_drive\Songs\songsList.txt"
LAST_UPDATED = "D:\Google_drive\Songs\LastUpdated.txt"
PAGES = 706


# PAGES = 2
# LAST_7_DAYS
# LAST_30_DAYS
# LAST_90_DAYS
# LAST_180_DAYS
# LAST_365_DAYS
# ALL

def get_file_path():
    return FILE_PATH


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


def get_songs():
    log("Generate songs list")
    log("Clear existing or create new file")
    open(FILE_PATH, 'w').close()
    for i in range(1, PAGES):
        titles = get_titles('https://www.last.fm/pl/user/TotaledThomas/library/tracks?page= %s' % str(i))
        to_file(titles)


def to_file(titles):
    with open(FILE_PATH, 'a') as f:
        for text in titles:
            try:

                f.write(text)
                f.flush()
            except Exception as ex:
                log("EXCEPTION while generating songs list")
                log(str(ex))
                continue


def update_songs():
    date_today = date.today()
    log("Update songs list")
    f1 = open(FILE_PATH)
    f2 = open(FILE_PATH, 'a')
    with (open(LAST_UPDATED, 'r')) as f3:
        if f3.readline() == str(date_today):
            log("List already updated")
            return 0
    log("Files opened Correctly")
    old_titles = [line for line in f1.readlines()]
    for i in range(1, 60):
        new_titles = get_titles(
            "https://www.last.fm/pl/user/TotaledThomas/library?date_preset=LAST_30_DAYSS&page=%s" % str(i))
        log("New titles: %s page %s" % (str(new_titles), str(i)))
        for title in new_titles:
            try:
                if title not in old_titles:
                    f2.write(title)
                    f2.flush()
            except Exception as ex:
                log("Error while updating songs list")
                log(str(ex))
                continue
    f2.flush()
    f2.close()
    log("Song List updated correctly")
    open(LAST_UPDATED, 'w').write(str(date_today))


if __name__ == '__main__':
    get_songs()

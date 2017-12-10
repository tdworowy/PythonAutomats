from datetime import date
from multiprocessing import Process
from shutil import copyfile

import requests
from bs4 import BeautifulSoup

from Utils.utils import log

FOLDER_PATH = "E:\Google_drive\Songs\\"
FILE_PATH = "E:\Google_drive\Songs\songsList.txt"
LAST_UPDATED = "E:\Google_drive\Songs\LastUpdated.txt"


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
    return int(max([page.text for page in pages[:-1]]))


def get_titles(url):
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


def get_songs(min, max, user='TotaledThomas', file_path=FILE_PATH):
    open(file_path, 'w').close()
    url = 'https://www.last.fm/pl/user/%s/library/tracks' % user
    titles_map = map(get_titles, [url + '?page= %s' % str(i) for i in range(min, max + 1)])
    for tiles_list in titles_map:
        to_file(tiles_list, file_path)


def to_file(titles, file_path):
    with open(file_path, 'a') as f:
        for text in titles:
            try:
                f.write(text)
                f.flush()
            except Exception as ex:
                log(str(ex))
                continue


def check_last_updated():
    date_today = date.today()
    with (open(LAST_UPDATED, 'r')) as f3:
        if f3.readline() == str(date_today):
            return True
        else:
            f3.write(str(date_today))
            return False


def remove_duplicates():
    uniq_lines = set(open(FILE_PATH).readlines())
    open(FILE_PATH, 'w').writelines(set(uniq_lines))


def _update_songs(min=1, max=60, user='TotaledThomas', file_path=FILE_PATH):
    if check_last_updated(): return 0
    url = "https://www.last.fm/pl/user/%s/library?date_preset=LAST_30_DAYSS" % user
    new_titles_map = map(get_titles, [url + "&page=%s" % str(i) for i in range(min, max + 1)])
    for tiles_list in new_titles_map:
        to_file(tiles_list, file_path)


def distribution(parts, min_=1, max=0, user_='TotaledThomas', target=get_songs):
    if max == 0:
        url = 'https://www.last.fm/pl/user/%s/library/tracks' % user_
        max = get_pages_count(url)
    rest = max % parts
    min = min_
    inc = (max - min_) // parts
    max = min_ + inc
    processes = []
    for i in range(1, parts + 1):
        if i == parts: max = max + rest
        process = Process(target=target, args=(min, max, user_, FOLDER_PATH + "songsList%s.txt" % str(i)))
        max = max + inc
        min = min + inc
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()


def update_songs_distribution():
    distribution(parts=6, max=60, target=_update_songs)
    remove_duplicates()


def combine_files(count, file_path=FILE_PATH):
    file_names = [FOLDER_PATH + "songsList%s.txt" % str(i) for i in range(1, count + 1)]
    with open(file_path, 'w') as outfile:
        for fname in file_names:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


if __name__ == '__main__':
    pool_count = 10

    distribution(pool_count)

    combine_files(pool_count)
    remove_duplicates()
    copyfile(FILE_PATH, "songs.txt")

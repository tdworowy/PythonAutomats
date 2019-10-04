import os
from datetime import date
from enum import Enum
from multiprocessing import Process
from shutil import copyfile

import requests
from Utils.file_utils import to_file, remove_duplicates, combine_files, remove_files
from bs4 import BeautifulSoup

"""This module pares songs from lastfm profile to .txt file """

FOLDER_PATH = "E:\Google_drive\Songs\\"
LAST_UPDATED = "E:\Google_drive\Songs\LastUpdated.txt"


class Period(Enum):
    LAST_7_DAYS = "LAST_7_DAYS"
    LAST_30_DAYS = "LAST_30_DAYS"
    LAST_90_DAYS = "LAST_90_DAYS"
    LAST_180_DAYS = "LAST_180_DAYS"
    LAST_365_DAYS = "LAST_365_DAYS"
    ALL = "ALL"


def __get_pages_count(url: "url to lastfm pages list"):
    """Get number of pages."""
    try:
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        pagination_list = soup.find('ul', class_="pagination-list")
        pages = pagination_list.find_all('a')
    except AttributeError:
        return 0
    page_count = (max([int(page.text) for page in pages[:-1]]))
    return page_count


def get_pages_count(user_, all=True):
    if all:
        url = 'https://www.last.fm/pl/user/%s/library/tracks' % user_
    else:
        url = "https://www.last.fm/pl/user/%s/library?page=1&date_preset=%s" % (user_, Period.LAST_30_DAYS.value)
    return __get_pages_count(url)


def get_titles(url: "url to lastfm profile"):
    """Get songs titles."""
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    titles = soup.find_all("a", class_="link-block-target")
    titles = str(titles)
    titles = titles.split(">")
    return clear_titles(titles)


def clear_titles(titles: "titles list"):
    """Clear titles."""
    clean_titles = []
    title_1 = "title=\""
    title_2 = "title=\'"
    for text in titles:
        try:
            # print(text)
            if "—" in text:
                try:
                    i = text.index(title_1) + len(title_1)
                except ValueError:
                    i = text.index(title_2) + len(title_2)

                temp = text[i:-1].replace("—", "-")
                clean_titles.append(temp + "\n")

        except Exception as ex:
            print(ex)
            continue
    return clean_titles


def get_songs(min, max, user: "lastfm user name" = 'TotaledThomas', file_path: "path to songlist.txt" = FOLDER_PATH):
    """Get songs form lastfp user profile."""
    url = 'https://www.last.fm/pl/user/%s/library/tracks' % user
    titles_map = map(get_titles, [url + '?page= %s' % str(i) for i in range(min, max + 1)])
    for tiles_list in titles_map:
        to_file(tiles_list, file_path)


def check_last_updated():
    """Check last update time -- stored in txt file"""
    date_today = date.today()
    with (open(LAST_UPDATED, 'r')) as f:
        return f.readline() == str(date_today)


def save_last_updated():
    """Update last update time -- stored in txt file"""
    date_today = date.today()
    with open(LAST_UPDATED, 'w') as f:
        f.write(str(date_today))
    return False


def _update_songs(min=1, max=60, user: "lastfm user name" = 'TotaledThomas',
                  file_path: "path to songlist.txt" = FOLDER_PATH):
    """Update existing songs list (use songs from last 30 days)"""
    url = lambda i: "https://www.last.fm/pl/user/%s/library?page=%s&date_preset=%s" % (
        user, str(i), Period.ALL.value)
    new_titles_map = map(get_titles, [url(i) for i in range(min, max + 1)])
    for tiles_list in new_titles_map:
        to_file(tiles_list, file_path)


def distribution(parts, min_=1, max=0, user_: "lastfm user name" = 'TotaledThomas',
                 target: "target function" = get_songs, all=True, file="thomas"):
    """Use multiprocessing to speed up lastfm parsing."""
    if max == 0:
        max = get_pages_count(user_, all)
    rest = max % parts
    min = min_
    inc = (max - min_) // parts
    max = min_ + inc
    processes = []
    for i in range(1, parts + 1):
        if i == parts: max = max + rest
        process = Process(target=target, args=(min, max, user_, FOLDER_PATH + "%sList%s.txt" % (file, str(i))))
        max = max + inc
        min = min + inc
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()


def generate_file(count, name):
    file_path = os.path.join(FOLDER_PATH, "%sList.txt" % name)
    combine_files(count, file_path, FOLDER_PATH, "%sList" % name, 'a')
    remove_files([r'%s\%sList%s.txt' % (FOLDER_PATH, name, i) for i in range(1, count + 1)])
    remove_duplicates(file_path)
    copyfile(file_path, "%s.txt" % name)


def update_songs_distribution():
    """Use multiprocessing to speed up lastfm parsing."""
    if check_last_updated():
        return 0
    pool_count = 10
    distribution(parts=pool_count, user_='TotaledThomas', target=get_songs, all=True, file="thomas")
    distribution(parts=pool_count, user_='theRoobal', target=get_songs, all=True, file="roobal")
    generate_file(pool_count, "thomas")
    generate_file(pool_count, "roobal")
    save_last_updated()


def get_all_songs():
    pool_count = 10

    open(FOLDER_PATH, 'w').close()
    distribution(parts=pool_count, user_='TotaledThomas', target=get_songs)
    distribution(parts=pool_count, user_='theRoobal', target=get_songs)

    combine_files(pool_count, FOLDER_PATH, FOLDER_PATH, "songsList")
    remove_files([r'%s\songsList%s.txt' % (FOLDER_PATH, i) for i in range(1, pool_count + 1)])
    remove_duplicates(FOLDER_PATH)
    copyfile(FOLDER_PATH, "songs.txt")
    save_last_updated()


if __name__ == '__main__':
    get_all_songs()

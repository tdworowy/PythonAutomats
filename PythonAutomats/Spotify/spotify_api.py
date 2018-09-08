import os
import time
from multiprocessing import Process

import spotipy
from Utils.file_utils import combine_files, create_file_if_not_exist, remove_duplicates
from Utils.utils import MyLogging
from spotipy import util

SONGS_PATH = "E:\Google_drive\Songs\songsList.txt"
FOLDER_PATH = "E:\Google_drive\Songs\\"
FILE_PATH = "E:\Google_drive\Songs\songsIDs.txt"

#https://developer.spotify.com/dashboard/applications/c70703140d1847f8a3260cd112565fbd

class SpotifyApi:

    def __init__(self, user_name, client_id, client_secret, redirect_uri):
        self.mylogging = MyLogging()
        self.user_name = user_name
        token = self.get_token(user_name, client_id, client_secret, redirect_uri)
        self.sp = spotipy.Spotify(auth=token)

    def get_token(self, user_name, client_id, client_secret, redirect_uri):
        """https://developer.spotify.com/web-api/using-scopes/"""
        scope = 'playlist-modify-public'
        token = util.prompt_for_user_token(username=user_name, scope=scope, client_id=client_id,
                                           client_secret=client_secret, redirect_uri=redirect_uri)
        if token:
            return token

        else:
            self.mylogging.log().info("Can't get token for: %s" % user_name)

    def get_playlists(self):
        return self.sp.current_user_playlists()

    def get_tracks_ids(self, tracks_list):
        id_map = map(self.sp.search, tracks_list)
        ids = []
        for track in list(id_map):
            try:
                ids.append(track['tracks']['items'][0]['id'])
            except Exception as ex:
                print(ex)
                continue
        return ids

    def save_tracks_ides_to_file(self, tracks_list, file_name):
        create_file_if_not_exist(file_name)
        with open(file_name, "a")as f1:
            for line in self.get_tracks_ids(tracks_list):
                f1.write(line + "\n")
                f1.flush()

    def create_playlist(self, name, public=True, ):
        user_id = sa.sp.current_user()['id']
        return self.sp.user_playlist_create(user_id, name, public)

    def add_tracks(self, play_list_id, tracks_ides):
        user_id = sa.sp.current_user()['id']
        try:
            self.sp.user_playlist_add_tracks(user=user_id, playlist_id=play_list_id, tracks=tracks_ides)
        except Exception as  ex:
            print(ex)
            pass

    def get_song_uri(self, song_id):
        return self.sp.track(song_id).strip()


def distribution(parts, target, tracks_list, min_=1, max=1):
    rest = max % parts
    min = min_
    inc = (max - min_) // parts
    max = min_ + inc
    processes = []
    for i in range(1, parts + 1):
        tracks_list_siced = tracks_list[min: max]
        if i == parts: max = max + rest
        process = Process(target=target, args=(tracks_list_siced, FOLDER_PATH + "song_ides%s.txt" % str(i)))
        max = max + inc
        min = min + inc
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()


def songs_ides_distributed(sa, start):
    with open(SONGS_PATH) as songs_file:
        count = sum(1 for line in songs_file)
        songs_file.seek(0)
        songs = songs_file.readlines()

    ides = start
    songs_count = ides + 200
    while ides < count:
        distribution(pool_count, sa.save_tracks_ides_to_file, songs, min_=ides, max=songs_count)
        ides = songs_count
        songs_count = songs_count + 200
        time.sleep(2)

    combine_files(pool_count, FILE_PATH, FOLDER_PATH, "song_ides")
    remove_duplicates(FILE_PATH)


if __name__ == "__main__":
    START = 0
    with open('auth.txt') as aut:
        user_name = aut.readline().strip()
        client_id = aut.readline().strip()
        client_secret = aut.readline().strip()
        redirect_uri = aut.readline().strip()

    pool_count = 10
    sa = SpotifyApi(user_name, client_id, client_secret, redirect_uri)

    if not os.path.isfile(FILE_PATH):
        songs_ides_distributed(sa, START)

    with open(FILE_PATH) as ides_list:
        ides = ides_list.readlines()
        ides_list.seek(0)
        count = sum(1 for line in ides_list)
        # print(sa.get_song_uri(ides[1].strip()))

    LIMIT = 10989

    start = 0
    stop = 99
    offset = 99
    playlist_count = 1
    play_list_id = sa.create_playlist("My_all%s" % str(playlist_count))['id']

    while stop <= count:
        ides_striped = [i.strip() for i in ides[start:stop]]
        sa.add_tracks(play_list_id, ides_striped)
        start = stop
        stop = stop + 99
        offset = offset + 99
        if offset >= LIMIT:
            playlist_count += 1
            play_list_id = sa.create_playlist("My_all%s" % str(playlist_count))['id']
            offset = 99
#TODO Dont't work
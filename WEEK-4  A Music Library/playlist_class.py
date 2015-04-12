#!/usr/bin/python3
from songs_class import Songs
import datetime
import copy
import random
from tabulate import tabulate
import json
import os


class Playlist():

    def __init__(self, name="Unknow Playlist", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.rocklist = []
        self.song_number = 0
        self.first_random = True

    def is_a_song(self, song):
        if isinstance(song, Songs):
            return True
        return False

    def add_song(self, song):
        if self.is_a_song(song):
            self.rocklist.append(song)
        else:
            raise TypeError

    def remove_song(self, song):
        if self.is_a_song(song) and song in self.rocklist:
            self.rocklist.remove(song)
        else:
            raise TypeError

    def get_total_length(self):
        total_secs = 0
        for song in self.rocklist:
            total_secs += song.get_length(seconds=True)
        return str(datetime.timedelta(seconds=total_secs))

    def get_artists(self):
        artista = {}
        for songs in self.rocklist:
            if songs.artist in artista:
                artista[songs.artist] += 1
            else:
                artista[songs.artist] = 1
        return artista

    def next_song(self):
        if self.shuffle is False:
            if self.song_number < len(self.rocklist):
                self.current_song = self.rocklist[self.song_number]
                self.song_number += 1
                return self.current_song
            elif self.repeat is True and self.song_number == len(self.rocklist):
                self.song_number = 0
                self.current_song = self.rocklist[self.song_number]
                self.song_number += 1
                return self.current_song
            else:
                raise NoMoreSongsInPlaylist

        elif self.shuffle is True:
            if self.first_random is True:
                self.random_list = copy.deepcopy(self.rocklist)
                self.first_random = False

            if len(self.random_list) == 0 and self.repeat is False:
                raise NoMoreSongsInPlaylist
            elif len(self.random_list) == 0 and self.repeat and not self.first_random:
                self.random_list = copy.deepcopy(self.rocklist)

            if len(self.random_list) > 0:
                self.current_song = random.choice(self.random_list)
                self.random_list.remove(self.current_song)

        return self.current_song

    def pprint_playlist(self):
        pptable = []
        headers = ["Artist", "Album", "SongTitle", "length"]
        for song in self.rocklist:
            pptable.append([song.artist, song.album, song.title, song.length])
        print (tabulate(pptable, headers, tablefmt="fancy_grid"))

    def save(self):
        directory = "playlists/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        plistname = directory + self.name.replace(" ", "-") + ".json"
        sfplist = {}
        sfplist["Playlist Name"] = self.name
        sfplist["repeat"] = self.repeat
        sfplist["shuffle"] = self.shuffle
        sfplist["Songs"] = []
        for song in self.rocklist:
            sfplist["Songs"].append({"artist": song.artist, "album": song.album, "title": song.title, "length": song.length})

        json_string = json.dumps(sfplist, indent=4)
        with open(plistname, "w") as f:
            f.write(json_string)

    @staticmethod
    def load(pl_name):
        directory = "playlists/"
        if not os.path.isfile(pl_name):
            pl_name = directory+pl_name
            if not os.path.isfile(pl_name):
                raise NoSuchPlaylist
        data = {}
        with open(pl_name, 'r') as fp:
            data = json.load(fp)
        loaded_playlist = Playlist(data["Playlist Name"], data["repeat"], data["shuffle"])
        for song in data["Songs"]:
            loaded_playlist.add_song(Songs(song["title"], song["artist"], song["album"], song["length"]))

        return loaded_playlist


class NoMoreSongsInPlaylist(Exception):
    pass


class NoSuchPlaylist(Exception):
    pass

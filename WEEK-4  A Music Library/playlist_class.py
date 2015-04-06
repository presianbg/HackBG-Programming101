#!/usr/bin/python3
from songs_class import Songs
import datetime


class Playlist():

    def __init__(self, name="Unknow Playlist", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.rocklist = []

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

    def get_total_lenght(self):
        self.total_secs = 0
        for song in self.rocklist:
            self.total_secs += song.get_lenght(seconds=True)
        return str(datetime.timedelta(seconds=self.total_secs))

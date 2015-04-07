#!/usr/bin/python3
from songs_class import Songs
import datetime
import copy
import random
from tabulate import tabulate


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

    def get_total_lenght(self):
        self.total_secs = 0
        for song in self.rocklist:
            self.total_secs += song.get_lenght(seconds=True)
        return str(datetime.timedelta(seconds=self.total_secs))

    def get_artists(self):
        self.artista = {}
        for songs in self.rocklist:
            if songs.artist in self.artista:
                self.artista[songs.artist] += 1
            else:
                self.artista[songs.artist] = 1
        return self.artista

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
        self.pptable = []
        self.headers = ["Artist", "Album", "SongTitle", "Lenght"]
        for song in self.rocklist:
            self.pptable.append([song.artist, song.album, song.title, song.lenght])
        print (tabulate(self.pptable, self.headers, tablefmt="fancy_grid"))


class NoMoreSongsInPlaylist(Exception):
    pass



def main():
    rock_song = Songs(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy", lenght="4:28")
    roll_song = Songs(title="Final Masquerade", artist="Linkin Park", album="The Hunting Party", lenght="3:34")
    rock_rolla = Songs(title="Knocking On Heaven's Door", artist="Guns N' Roses", album="Live concert", lenght="5:22")
    musiclist = Playlist(repeat=True, shuffle=True)
    musiclist.add_song(rock_song)
    musiclist.add_song(roll_song)
    musiclist.add_song(rock_rolla)
    musiclist.pprint_playlist()
    print(str(musiclist.next_song()))
    print(str(musiclist.next_song()))
    print(str(musiclist.next_song()))

if __name__ == '__main__':
    main()

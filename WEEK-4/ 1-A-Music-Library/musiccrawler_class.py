#!/usr/bin/python3
from playlist_class import Playlist
from songs_class import Song
import mutagen
import os
import datetime


class MusicCrawler:

    def __init__(self, dir_path=os.path.expanduser("~/Music")):
        self.dir_path = dir_path
        self.song_lst = []
        self.songtypes = ('.ogg', '.mp3', '.flac')
        self.find_songs()

    def find_songs(self):
        for root, dirs, files in os.walk(self.dir_path):
            for fn in files:
                path = os.path.join(root, fn)
                if fn.endswith(self.songtypes):
                    song = mutagen.File(path, easy=True)
                    self.song_lst.append(Song(song['title'][0], song['artist'][0], song['album'][0], str(datetime.timedelta(seconds=int(song.info.length))), path))

    def generate_playlist(self, plname="", shuff=False, repp=True):
        gn_plist = Playlist(name=plname, shuffle=shuff, repeat=repp)
        for s in self.song_lst:
            gn_plist.add_song(s)
        return gn_plist

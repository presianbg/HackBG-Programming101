#!/usr/bin/python3
import time
import datetime
import re


class Song:

    def __init__(self, title="Unknown Title", artist="Unkown Artist", album="Unkown Album", length="00:00", songpath=""):
        format_length = r"^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"
        if not re.match(format_length, length):
            raise ValueError

        if type(title) is not str or type(artist) is not str or type(album) is not str or type(length) is not str:
            raise TypeError

        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.songpath = songpath

    def __repr__(self):
        return "Song('{}', '{}', '{}')".format(self.title, self.artist, self.album, self.length)

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __hash__(self):
        return hash(self.title + self.length + self.artist)

    def __eq__(self, other):
        equal_title = self.title == other.title
        equal_artist = self.artist == other.artist
        if equal_title and equal_artist:
            return True
        return False

    def convert_to_sec(self):
        if self.length.count(':') == 1:
            x = time.strptime(self.length, '%M:%S')
            return int(datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds())
        elif self.length.count(':') == 2:
            x = time.strptime(self.length, '%H:%M:%S')
            return int(datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds())

    def get_length(self, seconds=False, minutes=False, hours=False):
        if seconds is False and minutes is False and hours is False:
            return self.length
        elif seconds is True and minutes is False and hours is False:
            return self.convert_to_sec()
        elif seconds is False and minutes is True and hours is False:
            return self.convert_to_sec()//60
        elif seconds is False and minutes is False and hours is True:
            return self.convert_to_sec()//3600
        else:
            raise TypeError




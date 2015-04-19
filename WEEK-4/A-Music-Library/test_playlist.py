#!/usr/bin/python3
import unittest
from playlist_class import Playlist, NoMoreSongsInPlaylist
from songs_class import Song
import time


class TestingPlaylist(unittest.TestCase):

    def setUp(self):
        self.rock_song = Song(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy", length="4:28")
        self.roll_song = Song(title="Final Masquerade", artist="Linkin Park", album="The Hunting Party", length="3:34")
        self.rock_rolla = Song(title="Knocking On Heaven's Door", artist="Guns N' Roses", album="Live concert", length="5:22")
        self.musiclist = Playlist(name="Test Playlist")
        self.musiclist.add_song(self.rock_song)
        self.musiclist.add_song(self.roll_song)
        self.ne_e_pesen = 0

    def test_add_song(self):
        with self.assertRaises(TypeError):
            self.musiclist.add_song(self.ne_e_pesen)
        self.assertIn(self.rock_song, self.musiclist.rocklist)

    def test_remove_song(self):
        with self.assertRaises(TypeError):
            self.musiclist.remove_song(self.ne_e_pesen)
        self.musiclist.remove_song(self.rock_song)
        self.assertNotIn(self.rock_song, self.musiclist.rocklist)

    def test_get_total_length(self):
        self.assertEqual(self.musiclist.get_total_length(), "0:08:02")

    def test_artists_hist(self):
        self.musiclist.add_song(self.rock_rolla)
        artists = self.musiclist.get_artists()
        self.assertEqual(artists["Guns N' Roses"], 2)

    def test_next_song(self):
        self.assertEqual(self.musiclist.next_song(), self.rock_song)
        self.assertEqual(self.musiclist.next_song(), self.roll_song)
        with self.assertRaises(NoMoreSongsInPlaylist):
            self.musiclist.next_song()

    def test_next_song_repat(self):
        self.repeat_mlist = Playlist(repeat=True)
        self.repeat_mlist.add_song(self.rock_song)
        self.repeat_mlist.add_song(self.roll_song)
        self.repeat_mlist.add_song(self.rock_rolla)
        self.assertEqual(self.repeat_mlist.next_song(), self.rock_song)
        self.assertEqual(self.repeat_mlist.next_song(), self.roll_song)
        self.assertEqual(self.repeat_mlist.next_song(), self.rock_rolla)
        self.assertEqual(self.repeat_mlist.next_song(), self.rock_song)

    def test_next_song_random(self):
        self.shuffle_mlist = Playlist(shuffle=True)
        self.shuffle_mlist.add_song(self.rock_song)
        self.shuffle_mlist.add_song(self.roll_song)
        with self.assertRaises(NoMoreSongsInPlaylist):
            self.shuffle_mlist.next_song()
            self.shuffle_mlist.next_song()
            self.shuffle_mlist.next_song()

    def test_next_song_random_repat(self):
        self.repeat_mlist = Playlist(repeat=True, shuffle=True)
        self.repeat_mlist.add_song(self.rock_song)
        self.repeat_mlist.add_song(self.roll_song)
        self.repeat_mlist.add_song(self.rock_rolla)
        for i in range(10):
            print(self.repeat_mlist.next_song(), " - Repeat Test")

    def test_pprint_playlist(self):
        self.musiclist.add_song(self.rock_rolla)
        self.musiclist.pprint_playlist()

    def test_save_load(self):
        self.musiclist.save()
        loaded_list = Playlist.load("playlists/Test-Playlist.json")
        loaded_list.pprint_playlist()

    def test_load(self):
        p = Playlist.load("playlists/Test-Playlist.json")
        try:
            while True:
                print(p.next_song(), " - Loaded Test")
                time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    unittest.main()

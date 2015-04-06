#!/usr/bin/python3
import unittest
from playlist_class import Playlist
from songs_class import Songs

class TestingPlaylist(unittest.TestCase):

    def setUp(self):
        self.rock_song = Songs(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy", lenght="4:28")
        self.roll_song = Songs(title="Final Masquerade", artist="Linkin Park", album="The Hunting Party", lenght="3:34")
        self.musiclist = Playlist()
        self.musiclist.add_song(self.rock_song)
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

    def test_get_total_lenght(self):
        self.musiclist.add_song(self.roll_song)
        self.assertEqual(self.musiclist.get_total_lenght(), "0:08:02")

    def test_artist_hist(sefl):
        pass

if __name__ == '__main__':
    unittest.main()

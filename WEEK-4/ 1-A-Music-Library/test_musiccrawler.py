#!/usr/bin/python3
import unittest
from musiccrawler_class import MusicCrawler
from songs_class import Song


class TestingMusicCrawler(unittest.TestCase):

    def testing_find_songs(self):
        p = MusicCrawler("/home/pressian/Music/Guns N` Roses - Chinese Democracy")
        self.assertEqual(type(p.song_lst[0]), Song)

    def test_generate_playlist(self):
        crawler = MusicCrawler("/home/pressian/Music/ACDC Rock Or Bust [Full Album] 2014/")
        zrock = crawler.generate_playlist(plname="TestingMC")
        print(zrock.get_total_length())
        zrock.pprint_playlist()
        zrock.save()


if __name__ == '__main__':
    unittest.main()

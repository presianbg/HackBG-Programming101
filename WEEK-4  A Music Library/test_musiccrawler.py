#!/usr/bin/python3
import unittest
from musiccrawler_class import MusicCrawler
from songs_class import Songs


class TestingMusicCrawler(unittest.TestCase):

    def testing_find_songs(self):
        p = MusicCrawler()
        self.assertEqual(type(p.song_lst[0]), Songs)


    def test_generate_playlist(self):
        crawler = MusicCrawler("/home/pressian/Music/Guns N` Roses - Chinese Democracy")
        zrock = crawler.generate_playlist()
        print(zrock.get_total_length())
        zrock.pprint_playlist()
        zrock.save()


if __name__ == '__main__':
    unittest.main()

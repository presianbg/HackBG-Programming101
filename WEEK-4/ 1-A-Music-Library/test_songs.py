#!/usr/bin/python3
import unittest
from songs_class import Song


class TestingSongs(unittest.TestCase):

    def setUp(self):
        self.rock = Song(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy", length="4:32",)

    def testing_init(self):
        with self.assertRaises(ValueError):
            self.roll = Song(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy - live", length="alabala")
        self.assertIsInstance(self.rock, Song)
        with self.assertRaises(TypeError):
            self.roll = Song(title=4, artist="Guns N' Roses", album=True, length="1:32:33")

    def test_str(self):
        self.assertEqual(str(self.rock), "Guns N' Roses - Shackler's Revenge from Chinese Democracy - 4:32")

    def test_hash(self):
        self.assertEqual(type(self.rock.__hash__()), int)

    def test_eq(self):
        self.roll = Song(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy - live", length="4:44")
        self.assertTrue(self.roll == self.rock)

    def test_length(self):
        self.assertEqual(self.rock.get_length(), "4:32")
        self.assertEqual(self.rock.get_length(seconds=True), 272)
        self.assertEqual(self.rock.get_length(minutes=True), 4)

if __name__ == '__main__':
    unittest.main()

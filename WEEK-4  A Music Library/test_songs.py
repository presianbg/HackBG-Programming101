#!/usr/bin/python3
import unittest
from songs_class import Songs


class TestingSongs(unittest.TestCase):

    def setUp(self):
        self.rock = Songs(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy", lenght="4:32")

    def testing_init(self):
        with self.assertRaises(ValueError):
            self.roll = Songs(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy - live", lenght="alabala")
        self.assertIsInstance(self.rock, Songs)
        with self.assertRaises(TypeError):
            self.roll = Songs(title=4, artist="Guns N' Roses", album=True, lenght="1:32:33")

    def test_str(self):
        self.assertEqual(str(self.rock), "Guns N' Roses - Shackler's Revenge from Chinese Democracy - 4:32")

    def test_hash(self):
        self.assertEqual(type(self.rock.__hash__()), int)

    def test_eq(self):
        self.roll = Songs(title="Shackler's Revenge", artist="Guns N' Roses", album="Chinese Democracy - live", lenght="4:44")
        self.assertTrue(self.roll == self.rock)

    def test_lenght(self):
        self.assertEqual(self.rock.get_lenght(), "4:32")
        self.assertEqual(self.rock.get_lenght(seconds=True), 272)
        self.assertEqual(self.rock.get_lenght(minutes=True), 4)

if __name__ == '__main__':
    unittest.main()

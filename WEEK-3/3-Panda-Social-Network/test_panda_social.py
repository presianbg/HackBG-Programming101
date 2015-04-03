#!/usr/bin/python3
from panda_social import Panda
from panda_social import InvalidMail, InvalidGender
import unittest


class TestingPanda(unittest.TestCase):
    def setUp(self):
        self.pandio = Panda("Pandio", "pandio@pandaland.cn", "male")

    def test_init(self):
        with self.assertRaises(TypeError):
            self.fake_pandio = Panda("Pan-Do", 5, 4.3)

    def test_str(self):
        self.assertEqual(str(self.pandio), "Hello, I'm Pandio, contact me at pandio@pandaland.cn, don't worry i'm male panda")

    def test_hash(self):
        self.assertEqual(type(self.pandio.__hash__()), int)

    def test_equal(self):
        self.fake_pandio = Panda("Pandio", "pandio@pandaland.cn", "male")
        self.assertEqual(self.pandio, self.fake_pandio)

    def test_email(self):
        with self.assertRaises(InvalidMail):
            self.fake_pandio = Panda("Pandio", "pandio$pandaland.cn", "male")
        self.assertEqual(self.pandio.email, "pandio@pandaland.cn")

    def test_gender(self):
        with self.assertRaises(InvalidGender):
            self.fake_pandio = Panda("Pandio", "pandio@pandaland.cn", "guru")
        self.assertEqual(self.pandio.gender, "male")

    def test_get_name(self):
        self.assertEqual(self.pandio.get_name(), "Pandio")

    def test_get_mail(self):
        self.assertEqual(self.pandio.get_mail(), "pandio@pandaland.cn")

    def test_get_gender(self):
        self.assertEqual(self.pandio.get_gender(), "male")

    def test_ask_gender(self):
        self.assertFalse(self.pandio.isFemale())
        self.assertTrue(self.pandio.isMale())


if __name__ == '__main__':
    unittest.main()

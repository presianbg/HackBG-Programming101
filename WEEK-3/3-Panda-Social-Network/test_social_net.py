#!/usr/bin/python3
from social_net import PandaSocialNetwork, PandaAlreadyThere, PandasAlreadyFriends
from panda_social import Panda
import unittest


class TestingSocialNet(unittest.TestCase):
    def setUp(self):
        self.pandanet = PandaSocialNetwork()
        self.pandio = Panda("Pandio", "pandio@pandaland.cn", "male")
        self.poonchoo = Panda("PoonChoo", "pandio@pandahomes.tw", "male")
        self.babameca = Panda("BabaMeca", "BabaMeca@gorata.bg", "female")
        self.tatkomechok = Panda("TatkoMeca", "TatkoMeca@gorata.bg", "male")
        self.pandanet.make_friends(self.pandio, self.poonchoo)

    def test_adding_panda(self):
        with self.assertRaises(PandaAlreadyThere):
            self.pandanet.add_panda(self.pandio)

    def test_has_panda(self):
        self.assertTrue(self.pandanet.has_panda(self.pandio))

    def test_add_friend(self):
        self.pandanet.add_friend(self.pandio, self.poonchoo)
        self.assertIn(self.poonchoo, self.pandanet.bambook_net[self.pandio])

    def test_are_friends(self):
        self.assertTrue(self.pandanet.are_friends(self.pandio, self.poonchoo))

    def test_make_fr(self):
        with self.assertRaises(PandasAlreadyFriends):
            self.pandanet.make_friends(self.pandio, self.poonchoo)
        self.pandanet.make_friends(self.pandio, self.babameca)
        self.assertTrue(self.pandanet.has_panda(self.babameca))
        self.assertTrue(self.pandanet.are_friends(self.pandio, self.babameca))

    def test_friends_of(self):
        self.assertFalse(self.pandanet.friends_of(self.babameca))
        self.assertEqual(type(self.pandanet.friends_of(self.pandio)), list)

    def test_connection_level(self):
        self.assertFalse(self.pandanet.connection_level(self.pandio, self.tatkomechok))
        self.pandanet.add_panda(self.tatkomechok)
        self.assertEqual(self.pandanet.connection_level(self.pandio, self.tatkomechok), -1)
        self.pandanet.make_friends(self.pandio, self.tatkomechok)
        self.assertEqual(self.pandanet.connection_level(self.poonchoo, self.tatkomechok), 2)

    def test_are_connected(self):
        self.pandanet.add_panda(self.tatkomechok)
        self.assertFalse(self.pandanet.are_connected(self.pandio, self.tatkomechok))

    def test_how_many_gender_in_network(self):
        self.assertEqual(self.pandanet.how_many_gender_in_network(1, self.pandio, "male"), 1)


if __name__ == '__main__':
    unittest.main()

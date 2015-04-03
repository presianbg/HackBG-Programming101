#!/usr/bin/python3
from panda_social import Panda


class PandaSocialNetwork():
    def __init__(self):
        self.bambook_net = {}

    def add_panda(self, panda):
        if type(panda) != Panda:
            raise ValueError
        if panda in self.bambook_net:
            raise PandaAlreadyThere
        self.bambook_net[panda] = []

    def has_panda(self, panda):
        if panda in self.bambook_net:
            return True
        return False

    def are_friends(self, panda1, panda2):
        if (panda2 in self.bambook_net[panda1]) and (panda1 in self.bambook_net[panda2]):
            return True
        return False

    def add_friend(self, panda, friend):
        self.bambook_net[panda].append(friend)
        self.bambook_net[friend].append(panda)

    def make_friends(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            if self.are_friends(panda1, panda2):
                raise PandasAlreadyFriends
            self.add_friend(panda1, panda2)
        elif not self.has_panda(panda1) and not self.has_panda(panda2):
            self.add_panda(panda1)
            self.add_panda(panda2)
            self.add_friend(panda1, panda2)
        elif not self.has_panda(panda1):
            self.add_panda(panda1)
            self.add_friend(panda1, panda2)
        elif not self.has_panda(panda2):
            self.add_panda(panda2)
            self.add_friend(panda1, panda2)

    def friends_of(self, panda):
        if not self.has_panda(panda):
            return False
        return self.bambook_net[panda]

    def connection_level(self, panda1, panda2):
        if panda1 not in self.bambook_net or panda2 not in self.bambook_net:
            return False
        if self.are_friends(panda1, panda2):
            return 1
        self.connection = self.find_connection(panda1, panda2)
        if not self.connection:
            return -1
        return (len(self.connection)-1)

    def find_connection(self, start, end, path=[]):
        path = path + [start]
        shortest = []
        if start == end:
            return path
        for pandas in self.bambook_net[start]:
            if pandas not in path:
                newpath = self.find_connection(pandas, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def are_connected(self, panda1, panda2):
        if self.find_connection(panda1, panda2):
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        if level == 1:
            self.gen_in_net = [pandas for pandas in self.bambook_net[panda] if pandas.gender == gender]
            return (len(self.gen_in_net))




class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass

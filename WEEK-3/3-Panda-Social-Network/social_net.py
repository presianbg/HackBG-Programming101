#!/usr/bin/python3
from panda_social import Panda
import json


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
        return self.connection

    def find_connection(self, start, end):
        self.visited = set()
        self.queue = []
        self.path_to = {}
        self.queue.append(start)
        self.visited.add(start)
        self.path_to[start] = None
        self.found = False
        self.path_lenght = 0

        while len(self.queue) != 0:
            self.current_node = self.queue.pop(0)
            if self.current_node == end:
                self.found = True
                break

            for neighbour in self.bambook_net[self.current_node]:
                if neighbour not in self.visited:
                    self.path_to[neighbour] = self.current_node
                    self.visited.add(neighbour)
                    self.queue.append(neighbour)

        if self.found:
            while self.path_to[end] is not None:
                self.path_lenght += 1
                end = self.path_to[end]
        return self.path_lenght

    def are_connected(self, panda1, panda2):
        if self.find_connection(panda1, panda2):
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        self.count = 0
        if level == 1:
            self.gen_in_net = [pandas for pandas in self.bambook_net[panda] if pandas.gender == gender]
            return (len(self.gen_in_net))

        self.visited = set()
        self.queue = []
        self.path_to = {}
        self.queue.append((0, panda))
        self.visited.add(panda)
        self.path_to[panda] = None
        self.count = 0

        while len(self.queue) != 0:
            self.data = self.queue.pop(0)
            self.current_lvl = self.data[0]
            self.current_node = self.data[1]

            if self.current_lvl > level:
                break

            if self.current_node != panda and self.current_lvl <= level and self.current_node.gender == gender:
                self.count += 1

            for neighbour in self.bambook_net[self.current_node]:
                if neighbour not in self.visited:
                    self.path_to[neighbour] = self.current_node
                    self.visited.add(neighbour)
                    self.queue.append((self.current_lvl + 1, neighbour))

        return self.count

    def save(self, path):
        self.safe_sn = {}
        for pandas in self.bambook_net:
            if repr(pandas) not in self.safe_sn:
                self.safe_sn[repr(pandas)] = []
            for friends in self.bambook_net[pandas]:
                self.safe_sn[repr(pandas)].append(repr(friends))

        json_string = json.dumps(self.safe_sn, indent=4)

        with open(path, "w") as f:
            f.write(json_string)
        print ("BamBook.net Saved Succesfuly in {}".format(path))

    def load(self, path):
        self.data = {}

        with open(path, 'r') as fp:
            self.data = json.load(fp)

        for pandas in self.data:
            self.add_panda(eval(pandas))
            for friends in self.data[pandas]:
                self.bambook_net[eval(pandas)].append(eval(friends))
        print ("BamBook.net Loaded Succesfuly from {}".format(path))


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass

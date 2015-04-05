#!/usr/bin/python3
from social_net import PandaSocialNetwork
from panda_social import Panda


def main():
    bambooknet = PandaSocialNetwork()

    bambooknet.load("test_write")

    print(bambooknet.are_friends(Panda('TatkoMeca', 'TatkoMeca@gorata.bg', 'male'), Panda('Pressy', 'press@dotaforpanda.cn', 'male')))


if __name__ == '__main__':
    main()

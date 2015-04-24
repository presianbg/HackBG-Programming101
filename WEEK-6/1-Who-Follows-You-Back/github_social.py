import requests
import json
from graph_module import DirectedGraph


class GitHubSocial:

    def __init__(self, user, level):
        self.user = user
        self.level = level

    def get_network_for(self, user):

        ff_network = {
            'followers': [],
            'following': []
        }

        conf = self.load_config()
        secret = conf['client_secret']
        client = conf['client_id']

        followers = requests.get('https://api.github.com/users/'
                                 + user +
                                 '/followers?client_id='
                                 + client +
                                 '&client_secret='
                                 + secret)

        following = requests.get('https://api.github.com/users/'
                                 + user +
                                 '/following?client_id='
                                 + client +
                                 '&client_secret='
                                 + secret)

        ff_network['followers'] = self.make_list_of_usernames(followers)
        ff_network['following'] = self.make_list_of_usernames(following)

        return ff_network

    def make_list_of_usernames(self, source):
        return [user['login'] for user in source.json()]

    def load_config(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config

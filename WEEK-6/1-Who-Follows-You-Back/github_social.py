import requests
import json
from graph_module import DirectedGraph


class GitHubSocial:

    def __init__(self):
        pass

    def _make_list_of_usernames(source):
        return [user['login'] for user in source.json()]

    def _load_config(filename):
        with open(filename, 'r') as f:
            config = json.load(f)
        return config

    @staticmethod
    def get_network_for(user):

        ff_network = {
            'followers': [],
            'following': []
        }

        conf = GitHubSocial._load_config('config.json')
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

        ff_network['followers'] = GitHubSocial._make_list_of_usernames(followers)
        ff_network['following'] = GitHubSocial._make_list_of_usernames(following)

        return ff_network

    @staticmethod
    def build_github_social(user, level):
        visited = set()
        queue = []
        github_graph = DirectedGraph()
        visited.add(user)
        queue.append((0, user))

        while len(queue) != 0:
            current_lvl, current_node = queue.pop(0)

            if current_lvl > level:
                break

            user_ff_net = GitHubSocial.get_network_for(current_node)

            for following in user_ff_net['following']:
                github_graph.add_edge(current_node, following)
                if following not in visited:
                    visited.add(following)
                    queue.append((current_lvl + 1, following))

            for follower in user_ff_net['followers']:
                github_graph.add_edge(follower, current_node)
                if follower not in visited:
                    visited.add(follower)
                    queue.append((current_lvl + 1, follower))

        return github_graph

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
        cur_followers_page = 1
        cur_following_page = 1
        is_there_followers = True
        is_there_following = True

        while is_there_followers:
            followers = requests.get('https://api.github.com/users/'
                                     + user +
                                     '/followers?page={}&client_id='.format(cur_followers_page)
                                     + client +
                                     '&client_secret='
                                     + secret)
            if followers.json():
                ff_network['followers'] += GitHubSocial._make_list_of_usernames(followers)
            else:
                is_there_followers = False
            cur_followers_page += 1

        while is_there_following:
            following = requests.get('https://api.github.com/users/'
                                     + user +
                                     '/following?page={}&client_id='.format(cur_following_page)
                                     + client +
                                     '&client_secret='
                                     + secret)
            if following.json():
                ff_network['following'] += GitHubSocial._make_list_of_usernames(following)
            else:
                is_there_following = False

            cur_following_page += 1

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

            for follower in user_ff_net['followers']:
                github_graph.add_edge(follower, current_node)
                if follower not in visited:
                    visited.add(follower)
                    queue.append((current_lvl + 1, follower))

            for following in user_ff_net['following']:
                github_graph.add_edge(current_node, following)
                if following not in visited:
                    visited.add(following)
                    queue.append((current_lvl + 1, following))

        return github_graph

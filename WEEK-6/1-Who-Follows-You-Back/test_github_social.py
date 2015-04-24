import unittest
from github_social import GitHubSocial


class TestGitHubSocial(unittest.TestCase):

    def test_get_network_for(self):
        test_social = GitHubSocial('presianbg', 3)
        print(test_social.get_network_for('presianbg'))


if __name__ == "__main__":
    unittest.main()

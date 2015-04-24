import unittest
from github_social import GitHubSocial


class TestGitHubSocial(unittest.TestCase):

    def test_get_network_for(self):
        #print(GitHubSocial.get_network_for('Lekensteyn'))
        pass

    def test_build_github_social(self):
        z = GitHubSocial.build_github_social('presianbg', 0)
        print(z.graph)


if __name__ == "__main__":
    unittest.main()

import unittest
from github_social import GitHubSocial


class TestGitHubSocial(unittest.TestCase):

    def test_get_network_for(self):
        self.assertEqual(len(GitHubSocial.get_network_for('presianbg')['followers']), 4)

    def test_build_github_social(self):
        z = GitHubSocial.build_github_social('presianbg', 0)
        self.assertTrue(z.path_between('sevgo', 'presianbg'))
        print(z)


if __name__ == "__main__":
    unittest.main()

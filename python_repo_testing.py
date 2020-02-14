import unittest
import python_repo_visual as pr


class PythonRepoTestCase(unittest.TestCase):
    """Test for python_repo_visual.py."""

    def setUp(self):
        """Call all the functions here, and test elements separately."""
        self.resp_obj = pr.get_response()
        self.repo_dictionaries = pr.get_repo_dicts()
        self.repo_dict = self.repo_dictionaries[0]
        self.repos_links, self.stars, self.label_s = pr.get_repo_data()

    def test_get_response(self):
        """Test that we get a valid response."""
        self.assertEqual(self.resp_obj.status_code, 200)

    def test_repo_dicts(self):
        """Test that we're getting the data we think we are."""
        # We should get dicts for 30 repositories.
        self.assertEqual(len(self.repo_dictionaries), 30)

        # Repositories should have required keys.
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())


if __name__ == '__main__':
    unittest.main()

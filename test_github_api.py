import unittest
from github_api import get_last_commit, get_issues

class TestGithubApiCalls(unittest.TestCase):
  def test_commit_obj_is_not_none(self):
    """Test for non-empty 'commit object'"""
    self.assertIsNotNone(get_last_commit())

  def test_commit_message_is_not_none(self):
    """Test for non-empty 'commit message'"""
    self.assertIsNotNone(get_last_commit().get("message"))

  def test_commit_sha_is_not_none(self):
    """Test for non-empty 'commit sha'"""
    self.assertIsNotNone(get_last_commit().get("sha"))

  def test_issue_list_is_not_none(self):
    """Test for non-empty 'issue list'"""
    self.assertIsNotNone(get_issues())

  def test_issue_list_is_not_empty(self):
    """Test for 'issue list' has at least 1 issue"""
    self.assertGreaterEqual(len(get_issues()),1)



if __name__ == "__main__":
    unittest.main(verbosity=2)



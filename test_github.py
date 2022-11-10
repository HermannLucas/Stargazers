import unittest
from unittest.mock import patch

import github

class TestGithub(unittest.TestCase):

  @patch('github._get_json_resp')
  def test_user_stars(self, mock_get_json_resp):
    test_user = "test_user"
    test_repo_name = "test_repo_name"
    test_repo_owner = "test_repo_owner"
    test_auth_token = "test_auth_token"
    
    mock_get_json_resp.side_effect = [[
      {
        'name': test_repo_name,
         'owner': {'login': test_repo_owner}
      }
    ]]

    expected_url = f"https://api.github.com/users/{test_user}/starred"
    expected_resp = [{'name': test_repo_name, 'owner': test_repo_owner}]
    
    resp = github.get_stars(test_user, test_auth_token)
    
    self.assertEqual(expected_resp, resp)
    mock_get_json_resp.assert_called_once_with(expected_url, test_auth_token)

  @patch('github._get_json_resp')
  def test_get_stargazers(self, mock_get_json_resp):
    test_user = "test_user"
    test_repo_name = "test_repo_name"
    test_repo_owner = "test_repo_owner"
    test_auth_token = "test_auth_token"
    
    mock_get_json_resp.side_effect = [[
      {'login': test_user}
    ]]
  
    expected_url = f"https://api.github.com/repos/{test_repo_owner}/{test_repo_name}/stargazers"
    expected_resp = [test_user]
    
    resp = github.get_stargazers(test_repo_owner, test_repo_name, test_auth_token)
    
    self.assertEqual(expected_resp, resp)
    mock_get_json_resp.assert_called_once_with(expected_url, test_auth_token)

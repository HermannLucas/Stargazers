import unittest
from unittest.mock import patch

import src.neighbours as neighbours

class TestNeighbours(unittest.TestCase):

  @patch('src.neighbours.get_stars')
  def test_map_user_repos(self, mock_get_stars):
    test_user = "test_user"
    test_auth_token = "test_auth_token"
    test_repo_name1 = "test_repo_name1"
    test_repo_owner1 = "test_repo_owner1"
    test_repo_name2 = "test_repo_name2"
    test_repo_owner2 = "test_repo_owner2"

    mock_get_stars.side_effect = [[
      {'name': test_repo_name1, 'owner': test_repo_owner1},
      {'name': test_repo_name2, 'owner': test_repo_owner2},
    ]]

    expected_res = [
      (f"{test_repo_owner1}/{test_repo_name1}", test_user),
      (f"{test_repo_owner2}/{test_repo_name2}", test_user),
    ]

    res = neighbours._map_user_repos(test_user, test_auth_token)

    self.assertEqual(expected_res, res)
    mock_get_stars.assert_called_once_with(test_user, test_auth_token)

  @patch('src.neighbours._map_user_repos')
  @patch('src.neighbours.get_stargazers')
  def test_get_neighbours(self, mock_get_stargazers, mock_map_user_repos):
    test_auth_token = "test_auth_token"
    test_user1 = "test_user1"
    test_user2 = "test_user2"
    test_repo1 = "test_repo1"
    test_repo2 = "test_repo2"
    test_repo3 = "test_repo3"
    test_owner = "test_owner"
    test_request_repo = "test-request-reop"
    test_auth_token = "test_auth_token"

    mock_get_stargazers.side_effect = [[
      test_user1,
      test_user2,
    ]]

    mock_map_user_repos.side_effect = [
      [
        (test_repo1, test_user1),
        (test_repo2, test_user1),
        (test_repo3, test_user1),
      ],
      [
        (test_repo2, test_user2),
      ]
    ]

    expected_res = {
      test_repo1: [test_user1],
      test_repo2: [test_user1, test_user2],
      test_repo3: [test_user1],
    }

    res = neighbours.get_neighbours(test_owner, test_request_repo, test_auth_token)

    self.assertEqual(expected_res.keys(), res.keys())
    for k in res.keys():
      self.assertEqual(expected_res[k], res[k])
    
from collections import defaultdict

from github import get_stars, get_stargazers

def _map_user_repos(user, auth_token):
  return [(f"{repo['owner']}/{repo['name']}", user) for repo in get_stars(user, auth_token)]
  
def get_neighbours(owner, repo, auth_token):
  stargazers = get_stargazers(owner, repo, auth_token)

  # Map Repos and Users
  repo_user_tuple_set = [r for user in stargazers for r in _map_user_repos(user, auth_token)]
  
  # Reduce the Repo, User tuples using the Repo
  res = defaultdict(set)
  for (rep, user) in repo_user_tuple_set:
   res[rep].add(user)
  return res

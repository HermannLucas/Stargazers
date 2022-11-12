from requests import get

def _get_json_resp(url, auth_token):
  return get(url, headers={'Authorization': auth_token}).json()
  
def get_stars(user, auth_token):
  url = f"https://api.github.com/users/{user}/starred"
  json_resp = _get_json_resp(url, auth_token)
  return [{'name': r['name'], 'owner': r['owner']['login']} for r in json_resp]

def get_stargazers(owner, repo, auth_token):
  url = f"https://api.github.com/repos/{owner}/{repo}/stargazers"
  json_resp = _get_json_resp(url, auth_token)
  return [u["login"] for u in json_resp]

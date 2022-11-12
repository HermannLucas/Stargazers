from src.app import app
import json
import os

from src.neighbours import get_neighbours

@app.route('/repos/<user>/<repo>/starneighbours')
def get_neighbours_handler(user, repo):
  
  auth_token = f"Bearer {os.environ['GITHUB_ACCESS_TOKEN']}"
  neighbours = get_neighbours(user, repo, auth_token)
  
  response = [{"repo": k, "stargazers": v} for (k, v) in neighbours.items()]
  return json.dumps(response)

import requests
from .repos import Repos

def fetch_repos(username):
    URL = f'https://api.github.com/users/{username}/repos'
    req = requests.get(URL)
    for data in req.json():
        Repos(data)
    return data
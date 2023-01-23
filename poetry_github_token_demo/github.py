import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.github.com/repos/octocat/Spoon-Knife/issues"


def set_auth():
    try:
        github_token = os.environ.get("ACCESS_TOKEN")
        assert github_token
        headers = {"Authorization": f"token {github_token}"}
        login = requests.get("https://api.github.com/user", headers=headers)
        assert login.json().get('login')
    except AssertionError:
        return {}
    else:
        return headers


def check_auth():
    try:
        github_token = os.environ.get("ACCESS_TOKEN")
        login = requests.get("https://api.github.com/user", headers=headers)
        return login.json().get('login')
    except KeyError:
        return login.json().get('message')


headers = set_auth()


def f_auth(count):
    res = requests.get(url, headers=headers)
    print(f"{res.status_code} for {count}")
    res.raise_for_status()


def f_no_auth(count):
    res = requests.get(url)
    print(f"{res.status_code} for {count}")
    res.raise_for_status()


def call_github_api(with_auth=True, call_limit=100):
    count = 0
    if with_auth:
        api_func = f_auth
    else:
        api_func = f_no_auth
    for i in range(call_limit):
        count += 1
        api_func(count)

import os
from poetry_github_token_demo import github


def test_call_github_api():
    github.call_github_api(with_auth=True, call_limit=1)


def test_set_auth():
    headers = github.set_auth()
    assert isinstance(headers, dict)


def test_access_token():
    assert len(os.environ.get('ACCESS_TOKEN')) >= 10


def test_check_auth():
    auth_user = github.check_auth()
    assert auth_user == 'sabinem'

import os
from poetry_github_token_demo import github


def test_call_github_api():
    github.call_github_api(with_auth=True, call_limit=1)


def test_secret():
    os.environ.get('MY_TEST') == 'test'


def test_secret_my_token():
    assert len(os.environ.get('MY_TOKEN')) >= 10

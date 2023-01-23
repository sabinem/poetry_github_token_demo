from poetry_github_token_demo import github


def test_call_github_api():
    github.call_github_api(with_auth=True, call_limit=100)

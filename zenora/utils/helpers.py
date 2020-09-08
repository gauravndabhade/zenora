import typing
import requests


def fetch(url: str, headers: typing.Dict[str, str], params: typing.Dict[str, str] = {}) -> typing.Dict:
    r = requests.get(url=url, headers=headers, params=params)
    return r.json()

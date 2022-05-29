"""
Main worker that the other one's inherit.
Most everything should be abstract.
"""

import requests


class Worker:
    def __init__(self, api_key, method):
        self._params = {
            'api_key': api_key,
            'format': 'json',
            'method': method
        }

    def make_call(self, params):
        api_endpoint = 'http://ws.audioscrobbler.com/2.0/'
        tmp_params = {**self._params, **params}
        resp = requests.get(api_endpoint, params=tmp_params)
        if resp.status_code != 200:
            return None
        return resp.json()

    def add_params(self, params):
        self._params = {**self._params, **params}

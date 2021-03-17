import requests


class ServerApiConnector:

    def __init__(self, endpoint, token, token_header_key=None):
        self.endpoint = endpoint
        self.token = token
        self.token_header_key = token_header_key

    def get(self, query=None, headers=None):
        headers = headers or {}
        if self.token_header_key:
            headers.update({self.token_header_key: self.token})
        with requests.Session() as session:
            return session.get(self.endpoint, params=query,  headers=headers)

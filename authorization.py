from asyncio import Lock
from datetime import datetime, timedelta

from httpx import post

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

from settings import (TOKEN_URL, CLIENT_ID, CLIENT_SECRET, USER_NAME, PASSWORD)


class TokenManager:

    def __init__(self):
        self.expires_at = datetime.now() - timedelta(seconds=15)
        self.set_token()

    def set_token(self):
        # if datetime.now() > self.expires_at:
        _token = self.load_token()
        self.access_token = _token['access_token']
        self.refresh_token = _token['refresh_token']
        self.expires_in = _token['expires_in']
        self.expires_at = datetime.fromtimestamp(_token['expires_at']) - timedelta(seconds=15)

    @property
    def token(self):
        if datetime.now() > self.expires_at:
            self.set_token()

        return self.access_token

    @staticmethod
    def load_token():
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=CLIENT_ID))
        token = oauth.fetch_token(token_url=TOKEN_URL, username=USER_NAME, password=PASSWORD,
                                  client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

        return token

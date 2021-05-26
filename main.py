import requests
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

host = 'api-services.telecom.kz'

url_pattern = f'https://{host}/api/v1/citizen/phone-verification-state/{{}}/{{}}'

headers = {
    "accept": "application/json"
}

client_id = 10
client_secret = 'pu9YDWk4twQzM5zNtKJlyfBUrnphgkcebL4Ou8QO'
username = 'bigdata@telecom.kz'
password = 'P7hTMFv26i8QlVYLSBUi1uT1Cx5jE1WM'


iin = '900987654321'
phone = '77075554433'
oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
token = oauth.fetch_token(token_url=f'https://{host}/oauth/token', username=username, password=password,
                          client_id=client_id, client_secret=client_secret)
print(token)
headers['Authorization'] = 'Bearer {}'.format(token['access_token'])
# headers['Authorization'] = 'Bearer {}'.format(to)
try:
    url = url_pattern.format(iin, phone)
    print(url)
    r = requests.get(url, headers=headers)
    r.raise_for_status()
except Exception as e:
    print(r.status_code)
# print(token)
print(r.text)




import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_URI = os.getenv('TOKEN_URI')
HOST = os.getenv('HOST')
HEADERS = {
    "accept": "application/json"
}

TOKEN_URL = f'https://{HOST}{TOKEN_URI}'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')


URL_PATTERN = f'https://{HOST}/api/v1/citizen/phone-verification-state/{{}}/{{}}'

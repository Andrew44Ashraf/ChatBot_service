import secrets
from database import *


def generate_token():
  while True:
    access_token = secrets.token_urlsafe()

    if not token_exists(acess_token):
      break
  
  return access_token
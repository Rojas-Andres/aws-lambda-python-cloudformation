import jwt 
import datetime 
import os

SECRET_KEY = os.environ.get("SECRET_KEY")

def create_token(payload):
    token = jwt.encode(payload, SECRET_KEY , algorithm="HS256")
    return token

import os 
import jwt

SECRET_KEY = os.environ.get("SECRET_KEY")

def decode_token(token):
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    except Exception as e:
        print("Error: ", e)
        return False
import jwt 
import datetime 
import os
import boto3


SECRET_KEY = os.environ.get("SECRET_KEY")

def create_token(payload):
    token = jwt.encode(payload, SECRET_KEY , algorithm="HS256")
    return token


def SQS_send(message):
    try:
        sqs = boto3.client(
            'sqs',
            region_name=os.environ['ENV_AWS_REGION'],
            aws_access_key_id=os.environ['ENV_AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['ENV_AWS_SECRET_ACCESS_KEY']
        )
        send_message = sqs.send_message(
            QueueUrl=os.environ['SQS_URL'],
            MessageBody=message
        )
        return send_message
    except Exception as e:
        print(e)
        return False
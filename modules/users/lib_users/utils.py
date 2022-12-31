import jwt 
import datetime 
import os
import boto3


SECRET_KEY = os.environ.get("SECRET_KEY")

def upload_file(name, ext, data):
    try:
        s3_client = boto3.resource(
            's3',
            aws_access_key_id=os.environ.get('ENV_AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('ENV_AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get('ENV_AWS_REGION_NAME')
        )
        now = datetime.datetime.now().strftime("%y%m%d%H%M%S")
        filename = f"{name}-{now}.{ext}"
        s3_client.Bucket(os.environ.get('ENV_AWS_S3_BUCKET_NAME')).put_object(
            Key=filename, Body=data, ACL='public-read'
        )
    except Exception as e:
        print(e)


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
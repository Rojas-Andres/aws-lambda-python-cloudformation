import boto3
import os
import datetime

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
        return f"https://{os.environ.get('ENV_AWS_S3_BUCKET_NAME')}.s3.amazonaws.com/{filename}"
    except Exception as e:
        print(e)


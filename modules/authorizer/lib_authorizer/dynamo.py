import os
import boto3
from boto3.dynamodb.conditions import Attr

class Dynamo:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=os.environ['ENV_AWS_REGION'],
            aws_access_key_id=os.environ['ENV_AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['ENV_AWS_SECRET_ACCESS_KEY']
        )
        self.table = self.dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    def get_item_by_token(self, token):
        response = self.table.scan(
            FilterExpression=Attr('token').eq(token)
        )
        return response['Items'][0] if response['Items'] else None
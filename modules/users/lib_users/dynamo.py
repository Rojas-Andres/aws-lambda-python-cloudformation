import os
import boto3

class Dynamo:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=os.environ['AWS_REGION'],
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
        )
        self.table = self.dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    def put_item_dynamo_table(self, item):
        response = self.table.put_item(Item=item)
        return response
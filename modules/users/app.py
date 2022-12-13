import json
import os
from db.database import DataBase


def lambda_handler(event, context):
    print("Received event: ", event)
    print("Context: ", context)
    data = {}
    if event.get("path") == "/users" and event.get("httpMethod") == "GET":
        db = DataBase()
        users = db.get_users()
        data = {"users": [dict(user) for user in users]}
    elif event.get("path") == "/users" and event.get("httpMethod") == "POST":
        data = {"message": "CREATE USER"}
    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": 200,
        "body": json.dumps(data),
    }

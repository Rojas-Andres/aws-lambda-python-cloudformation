import json
import os
from db.database import DataBase


def lambda_handler(event, context):
    print("Received event: ", event)
    print("Context: ", context)
    data = {}
    status_code = 200
    try:
        db = DataBase()
        if event.get("path") == "/users" and event.get("httpMethod") == "GET":
            users = db.get_users()
            data = {"users": [dict(user) for user in users]}
        elif event.get("path") == "/users" and event.get("httpMethod") == "POST":
            body = json.loads(event.get("body"))
            if not body.get("nombre"):
                raise Exception("Nombre is required")
            elif not body.get("apellido"):
                raise Exception("Apellido is required")
            elif not body.get("ciudad"):
                raise Exception("Ciudad is required")
            print("Body: ", body)
            user = db.create_user(body)
            data = {"user": user}
    except Exception as e:
        data = {"message": str(e)}
        status_code = 400

    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": status_code,
        "body": json.dumps(data),
    }

import json
import os
from lib_users.database import DataBase
from lib_users.schemas import User, UpdateUser


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
            user = User(**body).dict()
            user = db.create_user(user)
            data = {"user": user}
        elif "/users/" in event.get("path") and event.get("httpMethod") == "PATCH":
            id = event.get("pathParameters").get("id")
            user = db.get_user_by_id(id)
            if not user:
                raise Exception("User not found")
            body = json.loads(event.get("body"))
            user = UpdateUser(**body).dict(exclude_none=True)
            if not user:
                raise Exception("No data to update")
            user_update = db.update_user(id, user)
            data = {"user": user_update}
        elif "/users/" in event.get("path") and event.get("httpMethod") == "DELETE":
            id = event.get("pathParameters").get("id")
            user = db.get_user_by_id(id)
            if not user:
                raise Exception("User not found")
            db.delete_user_by_id(id)
            data["message"] = "User deleted"
        elif "/users/" in event.get("path") and event.get("httpMethod") == "GET":
            id = event.get("pathParameters").get("id")
            user = db.get_user_by_id(id)
            if not user:
                raise Exception("User not found")
            data = {"user": dict(user)}
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

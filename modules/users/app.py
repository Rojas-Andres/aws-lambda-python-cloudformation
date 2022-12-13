import json
import os
from db.database import DataBase


def lambda_handler(event, context):
    print("Received event: ", event)
    print("Context: ", context)

    db = DataBase()
    users = db.get_users()
    list_users = []
    for i in users:
        list_users.append(
            {
                "id": i[0],
                "nombre": i[1],
                "apellido": i[2],
                "ciudad": i[3],
            }
        )
    return {
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "statusCode": 200,
        "body": json.dumps({"users": list_users}),
    }

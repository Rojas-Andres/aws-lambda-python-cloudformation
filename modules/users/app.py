def lambda_handler(event, context):
    print("Received event: ", event)
    print("Context: ", context)
    return {"statusCode": 200, "body": "Hola"}

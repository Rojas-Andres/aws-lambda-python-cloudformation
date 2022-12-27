
from lib_authorizer.utils import decode_token
from lib_authorizer.dynamo import Dynamo


def generate_policy(principal_id, effect):
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "execute-api:Invoke",
                "Effect": effect,
                "Resource": "*"
            }
        ]
    }
    auth_response = {
        "principalId": principal_id,
        "policyDocument": policy_document
    }
    return auth_response

def lambda_handler(event, context):
    print("Received event: ", event)
    print("Context: ", context)
    if event.get("type") == "TOKEN":
        token = event.get("authorizationToken")
        payload = decode_token(token)
        if not payload:
            return generate_policy("user", "Deny")
        dynamo = Dynamo()
        user = dynamo.get_item_by_token(token)
        if not user:
            return generate_policy("user", "Deny")
        return generate_policy(int(user.get("user_id")), "Allow")
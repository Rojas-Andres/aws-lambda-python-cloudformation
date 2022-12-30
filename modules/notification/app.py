import json
import sendgrid
from sendgrid.helpers.mail import Mail
import os


def send_email_create_user(payload):
    sengrid_api_key = os.environ.get("SENDGRID_API_KEY")
    sg = sendgrid.SendGridAPIClient(api_key=sengrid_api_key)
    from_email = os.environ.get("FROM_EMAIL")
    to_email = payload.get("email")
    subject = "Bienvenido a la plataforma"
    message = Mail(
        from_email=from_email,
        to_emails=[to_email],
        subject=subject,
        plain_text_content=f"Hola {payload.get('name')}, bienvenido a la plataforma"
    )
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return True

def lambda_handler(event, context):
    print("Received event: ", event)
    print("Context: ", context)
    if event.get('Records'):
        for record in event['Records']:
            payload = json.loads(record['body'])
            if payload.get("type") == "create_user":
                send_email_create_user(payload)
    elif event.get("resources"):
        if "user_created_today" in event.get("resources")[0]:
            pass
    else:
        return None
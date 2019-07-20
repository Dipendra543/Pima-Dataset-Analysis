import os
from twilio.rest import Client


def send_sms(message):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]

    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+16825514241",
        from_="+19728959063",
        body=f'Hey Buddy, The prediction for your diabetic diagnosis is: {message}'

    )



from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message_body = "still testing..."

message = client.messages.create(
  from_=f"whatsapp:{os.getenv('TWILIO_PHONE_NUMBER')}",
  body=f"{message_body}",
  to=f"whatsapp:{os.getenv('RECEIVER_PHONE_NUMBER')}"
)

print(message.sid)

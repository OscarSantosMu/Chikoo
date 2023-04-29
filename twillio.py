# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC01a324f7bb0dcceb216c28547f79bc01"
auth_token = "299d2b4b9bf1137d9e4f5a54fd39332f"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hola 👋 Soy Chikoo un asistente virtual que te ayudara a que tu proxima experiencia en un consultorio sea rapida y satisfactoria 🤗",
  from_="+15673722242",
  to="+529213043932"
)
print(message.sid)

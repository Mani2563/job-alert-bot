from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_WHATSAPP_NUMBER")  # e.g. 'whatsapp:+14155238886'

client = Client(account_sid, auth_token)

def send_whatsapp(to_number: str, message: str):
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_number,
            to=f"whatsapp:{to_number}"
        )
        print("✅ WhatsApp sent:", message.sid)
        return True
    except Exception as e:
        print("❌ Failed to send:", e)
        return False

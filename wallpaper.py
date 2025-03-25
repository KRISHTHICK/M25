from twilio.rest import Client

def send_whatsapp_message(to, image_url):
    account_sid = 'your-twilio-account-sid'
    auth_token = 'your-twilio-auth-token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Here is your creative wallpaper: {image_url}",
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        to=f'whatsapp:{to}'
    )
    return message.sid

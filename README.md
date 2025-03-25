# M25
Gen Ai

Creating a simple AI agent to interact with users, get their favorite color, generate a creative wallpaper, and send it to a specified person on WhatsApp involves multiple steps. Below is a high-level plan and the necessary code snippets to build this:

Create a Chatbot to Get User's Favorite Color:
Use a library like flask to create a web-based chatbot.
Use OpenAI API to interact with ChatGPT.
Generate Creative Wallpaper:
Use an image generation API or tool to create a wallpaper based on the color.
Send the Wallpaper via WhatsApp:
Use WhatsApp's API or a third-party service to send the image.
Step-by-Step Plan
Set up the Flask Web Server:

Install Flask using pip install flask.
Create a Chatbot to Get User's Favorite Color:

Python
from flask import Flask, request, jsonify
import openai
import requests

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = 'your-openai-api-key'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User: {user_message}\nAI:",
        max_tokens=100
    )
    ai_message = response.choices[0].text.strip()
    return jsonify({"message": ai_message})

if __name__ == '__main__':
    app.run(debug=True)
Generate Creative Wallpaper:

Use an image generation API like DALL-E or a similar service.
Here is an example using DALL-E.
Python
def generate_wallpaper(color):
    response = openai.Image.create(
        prompt=f"Create a creative wallpaper with the color {color}",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url
Send the Wallpaper via WhatsApp:

Use Twilio API for WhatsApp messaging.
Install Twilio using pip install twilio.
Python
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
Integrate Everything:

Complete the Flask app to interact with the user, generate the wallpaper, and send it.
Python
from flask import Flask, request, jsonify
import openai
import requests
from twilio.rest import Client

app = Flask(__name__)

# Configure OpenAI and Twilio API keys
openai.api_key = 'your-openai-api-key'
account_sid = 'your-twilio-account-sid'
auth_token = 'your-twilio-auth-token'
client = Client(account_sid, auth_token)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User: {user_message}\nAI:",
        max_tokens=100
    )
    ai_message = response.choices[0].text.strip()
    
    # Check for favorite color in the message
    if "favorite color is" in user_message.lower():
        color = user_message.split("favorite color is")[-1].strip()
        image_url = generate_wallpaper(color)
        to = request.json['to']
        message_sid = send_whatsapp_message(to, image_url)
        return jsonify({"message": f"Wallpaper generated and sent to {to}. Message SID: {message_sid}"})
    
    return jsonify({"message": ai_message})

def generate_wallpaper(color):
    response = openai.Image.create(
        prompt=f"Create a creative wallpaper with the color {color}",
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url

def send_whatsapp_message(to, image_url):
    message = client.messages.create(
        body=f"Here is your creative wallpaper: {image_url}",
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        to=f'whatsapp:{to}'
    )
    return message.sid

if __name__ == '__main__':
    app.run(debug=True)
Instructions for Setting Up
Set up the environment:

Install the necessary libraries: pip install flask openai twilio requests.
Configure API Keys:

Replace 'your-openai-api-key', 'your-twilio-account-sid', and 'your-twilio-auth-token' with your actual API keys.
Run the Flask App:

Execute the script: python app.py.
Interact with the Bot:

Use a tool like Postman to send POST requests to http://127.0.0.1:5000/chat with a JSON payload containing the user's message and the recipient's WhatsApp number.
This setup will allow the chatbot to get the user's favorite color, generate a creative wallpaper, and send it via WhatsApp.

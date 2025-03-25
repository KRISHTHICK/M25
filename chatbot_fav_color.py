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

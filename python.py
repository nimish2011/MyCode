pip install Flask

chatbot/
├── app.py
├── static/
│   └── style.css
└── templates/
    └── index.html
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.example.com/chat'  # Replace with your actual API endpoint

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    
    # Call your chatbot API here
    response = requests.post(API_URL, json={'message': user_message, 'api_key': API_KEY})
    
    if response.status_code == 200:
        bot_message = response.json().get('response', 'Sorry, I did not understand that.')
    else:
        bot_message = 'Error: Unable to get response from the chatbot API.'

    return jsonify({'message': bot_message})

if __name__ == '__main__':
    app.run(debug=True)

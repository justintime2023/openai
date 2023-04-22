from flask import Flask, jsonify, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/openai-response', methods=['POST'])
def get_openai_response():
    user_question = request.form['question']

    # Replace with your own API key from OpenAI
    api_key = ''

    # Define the API endpoint
    url = 'https://api.openai.com/v1/chat/completions'

    # Set up the headers with the API key
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer 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'
    }

    # Define the input parameters for the API
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{"role": "user", "content": user_question}],
        'temperature': 0.7
    }

    # Make the API request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Parse the response
    response_data = response.json()

    # Extract the response message
    response_message = response_data['choices'][0]['message']['content']

    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run()

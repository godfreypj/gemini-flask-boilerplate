import os

import google.generativeai as genai
from flask import Flask, jsonify, render_template, request, send_from_directory

from utils.load_training_data import load_training_data
from utils.load_prompt import load_prompt
from utils.format_response import format_response
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY', 'TODO')
MODEL = os.environ.get('MODEL', 'gemini-1.5-flash')
genai.configure(api_key=API_KEY)

app = Flask(__name__, template_folder='web')

# Swagger
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/api/generate", methods=["GET"])
def generate_api():
    if API_KEY == 'TODO':
        return jsonify({ "error": '''
            To get started, get an API key at
            https://g.co/ai/idxGetGeminiKey and enter it in
            .env
            '''.replace('\n', '') }), 400
    try:
        # Go get the training data
        training_data = load_training_data()
        if training_data.startswith("Error:"):
            return jsonify({ "error": training_data }), 500

        # Add that to the prompt
        content = load_prompt(training_data)
        if content.startswith("Error:"):
            return jsonify({ "error": content }), 500

        # Give it to the robot
        model = genai.GenerativeModel(model_name=MODEL)

        # Get the response
        ai_response = ""
        for chunk in model.generate_content(content, stream=True):
            ai_response += chunk.text

        # Parse it
        parsed_data = format_response(ai_response)
        if parsed_data.get("is_error", False):  
            return jsonify({"error": parsed_data.get("error_message")}), 404

        # Access and return the parsed data
        actual_data = parsed_data.get("data")
        return jsonify({"text": actual_data}), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        with app.app_context():
            return jsonify({ "error": str(e) })

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('web', path)

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 5000)))

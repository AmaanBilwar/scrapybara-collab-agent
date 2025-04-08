from flask import Flask, request, jsonify
from flask_cors import CORS
import os 
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"echo": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/scrape', methods=['POST'])
def scraper():
    data = request.json
    url = data.get('url')
    # Here you would add your scraping logic using Scrapybara or any other library.
    # For now, we'll just return the URL for demonstration purposes.


    return jsonify({"scraped_data": f"Scraped data from {url}"})




if __name__=='__main__':
    app.run(debug=True)

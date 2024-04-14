
from flask import Flask, request, jsonify
from pymongo import MongoClient
#add cors
from flask_cors import CORS
app = Flask(__name__)


CORS(app)
#allow all origins
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/',methods=['GET'])
def home():
    return "Hello World"


@app.route('/slack/events', methods=['POST'])
def add_data():
    try:
        print(request.json)
        return jsonify({"message":"Data received" + str(request.json)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)

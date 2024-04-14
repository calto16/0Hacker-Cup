import os
from pathlib import Path
from dotenv import load_dotenv
#add cors
from flask_cors import CORS

from flask import Flask, request, jsonify
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler


# Initialize Flask app and Slack app
app = Flask(__name__)
CORS(app)
#allow all origins
CORS(app, resources={r"/*": {"origins": "*"}})

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
slack_app = App(
                token=os.environ['BOT_TOKEN'],
                signing_secret=os.environ['SIGNING_SECRET']
            )


# Route for handling slash command requests
@app.route("/slack/command", methods=["POST"])
def command():
    # Parse request body data
    data = request.form

    # Call the appropriate function based on the slash command
    print(data)
    return jsonify({"text": data['text']+"hello"})



# Initialize SlackRequestHandler to handle requests from Slack
handler = SlackRequestHandler(slack_app)

if __name__ == "__main__":
    # Start the Flask app on port 5000
    app.run(host='0.0.0.0', port=10000, debug=True)

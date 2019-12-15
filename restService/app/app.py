from flask import Flask, jsonify
import logging as logger
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/')
def home():
    author = 'Nishant Baheti'
    currentTimestamp = str(datetime.now())
    project = "Flask RestFul API hosted in Docker Environment"

    return jsonify({
        "owner": author,
        "currentTimestamp": currentTimestamp,
        "Description": project
    }), 200


if __name__ == "__main__":

    logger.debug("Starting Flask Server")
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=True)

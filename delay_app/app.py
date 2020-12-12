from flask import Flask, jsonify
from flask import request

from . import utils

app = Flask(__name__)

@app.route('/get_delay', methods=['POST'])
def index():
    data = request.get_json(force=True)
    try:
        delay = utils.main(data)
        return jsonify({"delay":delay})
    except KeyError:
        return jsonify({"error": "the format of json's inputs is incorrect"})

if __name__ == "__main__":
    app.run()
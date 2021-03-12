from flask import Flask, jsonify
from flask import request

from . import utils

app = Flask(__name__)

@app.route('/get_tags', methods=['POST'])
def index():
    data = request.get_json(force=True)
    try:
        tags = utils.main(data)
        return jsonify({"tags":tags})
    except KeyError as e :
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
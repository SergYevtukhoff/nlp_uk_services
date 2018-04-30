import json
from flask import Flask, request

from processing import *


app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process():
	text = request.get_json(force=True).get('text', '')
	return json.dumps({'text': preprocess(text)}, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
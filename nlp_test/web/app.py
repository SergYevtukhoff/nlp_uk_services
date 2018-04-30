import json

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process():
	try:
		text = request.get_json(force=True).get('text', '')
		r = requests.post('http://pr:5000/process', json={'text': text})
		r = requests.post('http://sw:5001/remove_stopwords', json={'text': r.json()['text']})
		r = requests.post('http://lm:5002/lemmatize', json={'text': r.json()['text']})
		return json.dumps({'text': r.json()['text']}, ensure_ascii=False)
	except ConnectionError as e:
		return json.dumps(str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
import json

import pymorphy2
from flask import Flask, request


app = Flask(__name__)


@app.route('/lemmatize', methods=['POST'])
def lemmatize():
    request_json = request.get_json(force=True)
    text = request_json.get('text', '')
    result = {
        'text': get_norm(text)
    }
    return json.dumps(result, ensure_ascii=False)


def get_norm(text):
    return ' '.join([morph.parse(w)[0].normalized[0] for w in text.split()])

if __name__ == "__main__":
    global morph
    morph = pymorphy2.MorphAnalyzer(lang='uk')
    app.run(host="0.0.0.0", port=5002, debug=False)
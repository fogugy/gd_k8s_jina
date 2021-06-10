import os
from flask import Flask, Response, jsonify, request
from flask import render_template
import requests

PORT = os.environ['SERVICE_PORT']
JINA_PORT = os.environ['JINA_PORT']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello():
    item = {
        'tags': {
            'caption': 'None',
            'image': 'None',
        },
        'score': {
            'value': 'None'
        }
    }

    payload = 'Payload stub'
    return render_template('index2.html',
                           text='Multimodal neural search',
                           item=item,
                           payload=payload)


@app.route('/search', methods=['POST'])
def search():
    r_jina = requests.post(f'http://0.0.0.0:{JINA_PORT}/search', request.data)
    r = Response(
        r_jina.text,
        status=r_jina.status_code,
        content_type=r_jina.headers['content-type']
    )
    r.headers.add('Access-Control-Allow-Origin', '*')
    return r


@app.route('/ping', methods=['GET'])
def ping():
    return Response('pong', status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)

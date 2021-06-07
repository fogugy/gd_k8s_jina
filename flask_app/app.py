import os
from flask import Flask
from flask import jsonify
app = Flask(__name__)

PORT = os.environ['SERVICE_PORT']
JINA_PORT = os.environ['JINA__PORT_EXPOSE']

@app.route('/')
def hello():
    return f'Index, SERVICE_PORT: {PORT}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
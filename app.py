import json
import os

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return jsonify({
        'headers': dict(request.headers),
        'args': request.args,
        'form': dict(request.form),
        'json': request.json,
        'remote_user': request.remote_user
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)

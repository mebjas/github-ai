from flask import Flask
from flask import Response
from flask import request

import sys
sys.path.insert(0, '../issue classifier/svm/')
import classifier
import json

app = Flask(__name__)

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = None
    if 'issue' in request.args:
        issue = request.args['issue']
        data = {'classification'  : classifier.classify(issue)}
    else:
        data = {'error'  : True}

    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp
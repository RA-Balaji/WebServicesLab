import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from q1 import *
from q2 import *

app = flask.Flask(__name__,template_folder='template')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/Q1', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def q1():
    
    content = request.get_json()
    email = content['email']
    send_mail(email)
    return jsonify({"result": "success"})


@app.route('/Q2', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def q2():
    
    content = request.get_json()
    email = content['email']
    
    return jsonify({"otp":main_fun(email)})


app.run(host='127.0.0.1', port = 5010)
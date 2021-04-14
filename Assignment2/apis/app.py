import flask
import flask 
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from q1 import *
from q2 import *
from q3 import *
from q4 import *
from q5 import *

app = flask.Flask(__name__,template_folder='template')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/', methods=['GET'])
def home():
    return '''<h1>API homepage</h1>
<p>APIs for Assignment 2</p>'''

@app.route('/Q1', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def q1():
    
    content = request.get_json()
    curr = content['current']
    curr_unit = content['curr_unit']
    voltage = content['voltage']
    voltage_unit = content['voltage_unit']


    return jsonify({"result":calc([curr, curr_unit], [voltage, voltage_unit])})

@app.route('/Q1/amp', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def q1amp():
    
    content = request.get_json()
    curr = content['current']
    curr_unit = content['curr_unit']
    voltage = content['voltage']
    voltage_unit = content['voltage_unit']


    return jsonify({"result":calc2([curr, curr_unit], [voltage, voltage_unit])})

@app.route('/Q2', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def q2():
    
    content = request.get_json()
    inp1 = content['inp1']
    inp2 = content['num2']
    base = content['base']

    return jsonify({"log":calc_log(inp1), "ln":ln(inp1), "anti_log":anti_lg(base, inp2)})

@app.route('/Q3', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def q3():
    
    content = request.get_json()
    li = content['inp1']
    num2 = content['num2']
    n = content['n']

    return jsonify({"GCD":gcd(li[0], li[1]), "LCM":lcm(li[0], li[1]), "Squareroot":sq_rt(num2), 
                "Cuberoot":cube_rt(num2), "nroot":n_rt(num2, n)})

@app.route('/Q4/trig', methods=['POST']) 
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def q4trig():
    
    content = request.get_json()
    angle = content['angle']

    
    return jsonify({"sin":calc_sin(angle), "cos":calc_cos(angle), "tan":calc_tan(angle),
    "sec":secx(angle), "cosec":cosecx(angle), "cot":cotx(angle)})


@app.route('/Q4/inverse_trig', methods=['POST']) 
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def q4inverse():
    
    content = request.get_json()
    val = content['value']

    return jsonify({"arcsin":calc_arcsin(val), "arccos":calc_arccos(val), "arctan":calc_arctan(val)})
    

@app.route('/Q5', methods=['POST']) 
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def q5():
    
    content = request.get_json()
    list1 = content['list1']
    list2 = content['list2']
    list3 = content['list3']


    return jsonify({"std_deviation":std_deviation(list1), "variance":variation(list1), "linear_reg":linear_reg(list2, list3)})
    
app.run(host='127.0.0.1', port = 5010)
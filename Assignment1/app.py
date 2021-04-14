import flask
import flask 
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from num2words import num2words 
from q1 import *
from q2 import *
from q3 import *
from q5 import *
from q6 import *
from q7 import *
from q8 import *
from q9 import *
from q10 import *

app = flask.Flask(__name__,template_folder='template')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# date diff
@app.route('/difference', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def info():

    content = request.get_json()
    date1 = content['date1']
    date2 = content['date2']

    days = main_fun(date1, date2)
    return jsonify({"difference":str(days) + " days"})

@app.route('/union', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def union():
    print('at start')
    content = request.get_json()
    #print(type(content))

    a = content["A"]
    b = content["B"]
    #print(a)
    
    res = union_op(a, b)
    return jsonify({"result":res})

@app.route('/minus', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def diff():
    print('at start')
    content = request.get_json()
    #print(type(content))

    a = content["A"]
    b = content["B"]
    #print(a)
    
    res = diff_op(a, b)
    return jsonify({"result":res})

@app.route('/intersection', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type', 'Authorization'])
def intersect():
    print('at start')
    content = request.get_json()
    print(content)

    a = list(dict.fromkeys(content["A"]))
    b = list(dict.fromkeys(content["B"]))
    #print(a)
    
    res = intersect_op(a, b)
    return jsonify({"result":res})

@app.route('/transpose', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def transpose():
    print('at start')
    content = request.get_json()
    #print(type(content))

    a = content["matrix"]
    #print(a)
    
    res = transpose_op(a)
    return str(res)

@app.route('/up_right', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def left():
    print('at start')
    content = request.get_json()
    #print(type(content))

    a = content["matrix"]
    #print(a)
    
    res = upright_diag(a)
    return jsonify(res)

@app.route('/low_left', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def right():
    print('at start')
    content = request.get_json()
    #print(type(content))

    a = content["matrix"]
    #print(a)
    
    res = lowleft_diag(a)
    return jsonify(res)

@app.route('/swivel', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def swivel():
    print('at start')
    content = request.get_json()
    #print(type(content))

    a = content["matrix"]
    #print(a)
    
    res = rotate90Clockwise(a)
    return jsonify(res)

@app.route('/toword', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def words():

    content = request.get_json()
    num = content["number"]
    return {"words":num2words(num)}


@app.route('/enc', methods = ['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def enc_route():
    second_prime = 31
    data = request.json
    text = data["text"]
    first_prime = data["key"]
    public_key,private_key = generate_keypair(first_prime,second_prime)

    cipher = [(ord(char) ** public_key[0]) % public_key[1] for char in text]
    print(cipher)
    crypted = ' '.join(list(map(str, cipher)))
    return jsonify({"encrypted_text":crypted , "key" : private_key})

@app.route('/dec', methods = ['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def dec():
    data = request.json
    text = data["encrypted_text"]
    private_key = data["key"]
    text =  toIntList(text, " ")

    plain = [chr((char ** private_key[0]) % private_key[1]) for char in text]
    decrypted = ''.join(plain)
    return jsonify({"decrypted_text":decrypted})

@app.route('/checksum', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def checksum():

    content = request.get_json()
    sentence = content["sentence"]
    st = generate_check(sentence)
    return jsonify({"hexchecksum":st})

@app.route('/barcode', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def barc():

    content = request.get_json()
    word = content["word"]
    generate_fun(word)
    return jsonify({"result":"./UI/images/barcode/"+word+'.svg'})

@app.route('/qrcode', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def qr():

    content = request.get_json()
    s = content["word"]
    generate_qr(s)
    img_file = './UI/images/' + s + '.png'
    return jsonify({"result":img_file})

@app.route('/generate', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def genereate_otp():

    return jsonify({"OTP":generateOTP()})

@app.route('/captcha', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def captchart():
    print('at start')

    res = captcha()
    return jsonify({"result":res})


app.run(host='127.0.0.1', port = 5010)
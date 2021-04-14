import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import bz2
import lzma 
import deflate

app = flask.Flask(__name__,template_folder='template')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class node:
    def __init__(self, freq, char, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.huff = ''

global_node_res=[]
def traverse(node, val=''):
    newVal = val + str(node.huff)
    if(node.left):
        traverse(node.left, newVal)
    if(node.right):
        traverse(node.right, newVal)
    if(not node.left and not node.right):
        global_node_res.append(node.char+"->"+newVal)

@app.route('/Q1',methods = ['POST', 'GET'])
@cross_origin()
def huffman_technique():
     if request.method == 'POST':
        global global_node_res
        content = request.get_json()
        h_msg = content['huffman_message']
        all_freq={}
        for i in h_msg: 
            if i in all_freq: 
                all_freq[i] += 1
            else: 
                all_freq[i] = 1
        h_char=[]
        h_freq=[]
        for x in all_freq:
            h_char.append(x)
            h_freq.append(all_freq[x])
        print(h_char,h_freq)
        nodes = []
        for i in range(len(h_char)):
            nodes.append(node(h_freq[i], h_char[i]))
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            left = nodes[0]
            right = nodes[1]
            left.huff = 0
            right.huff = 1
            newNode = node(left.freq+right.freq, left.char+right.char, left, right)
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newNode)
        traverse(nodes[0])
        Ginput=[str(h_msg)]
        res=[global_node_res]
        global_node_res=[]
        output_json={"title":"huffman_technique","language":"Python","question":"huffman_technique","params":Ginput,"result":res,"status":200}
        output={"result":res,"status":200}
        return jsonify(output)

@app.route('/Q2',methods = ['POST', 'GET'])
@cross_origin()
def run_length_algorithm():
     if request.method == 'POST':
        content = request.get_json()
        msg = content['message']
        Ginput=[msg]
        res=[run_length_algorithm_encode(msg),run_length_algorithm_Decode(run_length_algorithm_encode(msg))]
        output={"result":res,"status":200}
        return jsonify(output)

def run_length_algorithm_encode(msg): 
    encoded_msg = "" 
    i = 0
    while (i <= len(msg)-1): 
        count = 1
        ch = msg[i] 
        j = i 
        while (j < len(msg)-1): 
            if (msg[j] == msg[j+1]): 
                count = count+1
                j = j+1
            else: 
                break
        encoded_msg=encoded_msg+ch+str(count) 
        i = j+1
    return encoded_msg 

def run_length_algorithm_Decode(msg): 
    decoded_msg = ""
    count='0'
    last_char=''
    for i in msg:
        if(str.isdigit(i)):
            count =count + i
        else:
            for j in range(int(count)):
                decoded_msg=decoded_msg+last_char
            last_char=i
            count="0"
    for j in range(int(count)):
        decoded_msg=decoded_msg+last_char
    return decoded_msg

@app.route('/Q3', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type','Authorization'])
def lzw():
    if request.method == "POST":
        data = request.get_json()
        msg = data["message"]
        Ginput = [msg]
        res = [
            lzw_compress(msg),
            lzw_decompress(lzw_compress(msg)),
        ]
        output = {"result": res, "status": 200}
        return jsonify(output)



def lzw_compress(uncompressed):
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    

    result = []
    for c in uncompressed:
        wc = w + c
        
        if wc in dictionary:
            print("yes--> ",wc)
            w = wc
        else:
            result.append(dictionary[w])
            print("no--> ",w,wc)
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    if w:
        result.append(dictionary[w])
    return result
 
 
def lzw_decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()


@app.route('/Q4',methods = ['POST', 'GET'])
@cross_origin(origin="*", headers=["Content-Type", "Authorization"])
def Lossless_Compressions():
     if request.method == 'POST':
        data = request.get_json()
        msg = data["message"]
        byte_Data=msg.encode('utf-8')
        bz2_cmped= bz2.compress(byte_Data)
        bz2_uncmped=bz2.decompress(bz2_cmped)
        obj = lzma.LZMACompressor()
        lzma_cmped=obj.compress(byte_Data)
        obj = lzma.LZMADecompressor()
        lzma_uncmped=obj.decompress(lzma_cmped)
        def_cmped = deflate.gzip_compress(byte_Data, 6)
        def_uncmped = deflate.gzip_decompress(def_cmped)
        res=[str(bz2_cmped),str(bz2_uncmped.decode('utf-8')),str(lzma_cmped),str(msg),str(def_cmped),str(def_uncmped.decode('utf-8'))]
        output={"result":res,"status":200}
        return jsonify(output) 

app.run(host='127.0.0.1', port = 5010)

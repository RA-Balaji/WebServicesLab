var express = require('express');
var app = express();
const cors = require('cors')
var router = express.Router();      
const { toInteger, toString, union, intersection, floor } = require('lodash');

app.use(cors())
app.use(express.json())

app.listen(3000, () =>{
    console.log('Api started');
});

class node {
    constructor(freq, char,left,right) {
      this.freq = freq;
      this.char = char;
      this.left = left;
      this.right = right;
      this.huff='';
    }
  }
let global_node_res=[]
app.post('/Q1/', function(req, res) {

    const request = req.body
    let message = request['huffman_message']
    var freq = {};
    for (var i=0; i<message.length;i++) {
        var character = message.charAt(i);
        if (freq[character]) {
           freq[character]++;
        } else {
           freq[character] = 1;
        }
    }
    let h_char=[]
    let h_freq=[]
    for (const val in freq) {
        h_char.push(val)
        h_freq.push(freq[val])
    }
    let nodes=[]
    for (var i=0; i<h_char.length;i++) {
            nodes.push(new node(h_freq[i], h_char[i],null,null))
    }
    console.log(nodes)
    while(nodes.length>1){   
        nodes.sort(function (a, b) {
            return a.freq - b.freq;
          });
        let left=new node
        left=nodes[0]
        let right=new node
        right=nodes[1]
        left.huff=0
        right.huff=1
        let newNode =new node(left.freq+right.freq, left.char+right.char, left, right)
        nodes.splice(0,2);
        nodes.push(newNode)
    }
    traverse(nodes[0],"")
    let result=[global_node_res]
    global_node_res=[]
    let output_json={
        "title":"huffman_technique",
        "language":"JavaScript",
        "question":"huffman_technique",
        "params":[message],
        "result":result,
        "status":200}
    let output={"data":output_json,"status":200}
    res.setHeader('Content-Type', 'application/json');
    res.send({"result":result[0]});
});
function traverse(node,val){
    let newVal = val + String(node.huff)
    if(node.left)
        traverse(node.left, newVal)
    if(node.right)
        traverse(node.right, newVal)
    if(node.left==null && node.right==null)
        global_node_res.push(node.char+"->"+newVal)
}

app.post('/Q2/', function(req, res) {
    const request = req.body
    let msg = request['message']
   
   
    let result=[run_length_algorithm_encode(msg),run_length_algorithm_Decode(run_length_algorithm_encode(msg))]
    let output_json={
        "title":"run_length_algorithm",
        "language":"JavaScript",
        "question":"run_length_algorithm",
        "params":[msg],
        "result":result,
        "status":200}
    let output={"data":output_json,"status":200}
    res.setHeader('Content-Type', 'application/json');
    res.send({"result":result[0]});
});

function run_length_algorithm_encode(msg){ 
    let encoded_msg = "" 
    let i = 0
    while (i <= (msg.length)-1){
        count = 1
        ch = msg[i] 
        j = i 
        while (j < (msg.length)-1){
            if (msg[j] == msg[j+1]){
                count = count+1
                j = j+1
            }
            else{
                break
            }
        }
        encoded_msg=encoded_msg+ch+String(count)
        i = j+1
    }
    return encoded_msg 
}
function run_length_algorithm_Decode(msg){
    let decoded_msg = ""
    let count='0'
    let last_char=''
    console.log(msg,msg.length)
    for (var i=0; i<msg.length;i++) {
        if(!isNaN(msg[i])){
            count =count + msg[i]
        }
        else{
             for (var j=0; j<toInteger(count);j++) {
                decoded_msg=decoded_msg+last_char
             }
            last_char=msg[i]
            count="0"
        }
    }
    for (var i=0; i<toInteger(count);i++) {
        decoded_msg=decoded_msg+last_char
    }
    return decoded_msg 
}
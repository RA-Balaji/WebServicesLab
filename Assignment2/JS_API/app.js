const express = require('express');
const api = express();
const cors = require('cors')


api.use(cors())
api.use(express.json())


//home_page 
api.listen(3000, () =>{
    console.log('Api started');
});


// -------------------------Question 1 ------------------------//


function calc(curr, volt){

    w = (curr[0] * volt[0])/(curr[1] * volt[1])
    
    return ([w/1000, w,w*1000])
}

//Q1
api.post('/Q1/',(req,res) =>{  

    const request = req.body
    curr = request['current']
    curr_unit = request['curr_unit']
    voltage = request['voltage']
    voltage_unit = request['voltage_unit']

    res.send({"result":calc([curr, curr_unit], [voltage, voltage_unit])})
});


// -------------------------Question 2 ------------------------//
const LN10 = 2.3025850929940456840179914546844


function natural_log(x){
    var num ;
    num = (x - 1)/(x + 1);
    var sum = 0; 
    var old_sum = -1;
    for(var i = 1 ;sum != old_sum ; i++){
        old_sum = sum;
        denomiator = (2*i)-1;
        output = (num ** denomiator)/denomiator;
        sum += output
        
    }
    return 2*sum;
}

function common_log(x){
    if(x > 0){
        return (natural_log(x)/LN10);
    }
    return 0;
}



function anti_log(x,base){
    if(x > 0){
        return (base ** x);
    }
    return 0;
}


api.post('/Q2/',(req,res) =>{   
    const request = req.body;
    console.log(request);
    inp1 = request['inp1']
    inp2 = request['num2']
    base = request['base']

    res.send({"log":common_log(inp1), "ln":natural_log(inp1), "anti_log":anti_log(inp2, base)})
});



// -------------------------Question 3 ------------------------//



function GCF(num1, num2) {
    if(num2 == 0){
        return num1;
    }
    return GCF(num2,num1%num2);
  }



function LCM(num1, num2) {
    return ((num1 * num2) / GCF(num1, num2));
}



function sq_rt(num1) {
    return ((num1 ** (1/2)));
}



function cb_rt(num1) {
    return ((num1 ** (1/3)));
}


//nth root
function n_rt(num1,n) {
    return ((num1 ** (1/n)));
}


//Math-Log2 Calculator
api.post('/Q3/',(req,res) =>{
    const request = req.body;
    console.log(request);
    num1 = request['inp1'];
    num2 = request['num2'];
    n = request['n']
    res.send({"GCD":GCF(num1[0], num1[1]), "LCM":LCM(num1[0], num1[1]), "Squareroot":sq_rt(num2), 
    "Cuberoot":cb_rt(num2), "nroot":n_rt(num2, n)})
}); 


// -------------------------Question 4 ------------------------//
const PI = 3.14159;
const TAYLOR_TERMS = 10;
const TAYLOR_TERMS_ARCTAN = 50;


function fact(number){
    return (number <= 0 ) ? 1 : number * fact (number - 1);
}



function sinx(deg) {
    deg %= 360; 
    var rad = deg * PI / 180;
    var sin = 0;

    var i = 0;
    for(i = 0; i < TAYLOR_TERMS; i++) { 
        sin += ((-1) ** i) * ((rad**(2 * i + 1)) / fact(2 * i + 1));
    }
    return sin;
}

function cosx(deg) {
    deg %= 360; 
    var rad = deg * PI / 180;
    var cos = 0;

    var i = 0;

    for(i = 0; i < TAYLOR_TERMS; i++) { 
        cos += ((-1) ** i) * ((rad**(2 * i )) / fact(2 * i ));
    }
    return cos;
}

function tanx(deg) {
    if(( deg == 90) || (deg == 270)){
        return 'undefined';
    }
    return sinx(deg)/cosx(deg);
}

function secx(deg) {
    if(( deg == 90) || (deg == 270)){
        return 'undefined';
    }
    return 1/cosx(deg);
}

function cosecx(deg) {
    if(( deg == 0) || (deg == 180)){
        return 'undefined';
    }
    return 1/sinx(deg);
}

function cotx(deg) {
    if(( deg == 0) || (deg == 180)){
        return 'undefined';
    }
    return cosx(deg)/sinx(deg);
}

function arcsinx(x) {
    temp = x/((1- (x**2)) ** 0.5)
    return arctanx(temp);
}

function arccosx(x) {
    temp = ((1- (x**2)) ** 0.5)/x;
    console.log(temp)
    return arctanx(temp);
}

function arctanx(x) {
    var arctan = 0;
    var i = 0;
        for(i = 0; i < TAYLOR_TERMS_ARCTAN; i++) { 
            arctan += ((-1) ** i) * ((x**(2 * i + 1)) / (2 * i + 1));
        }
    return arctan*57.2958;
}


//Math-Log3 Calculator
api.post('/Q4/trig',(req,res) =>{   
    const Numbers = req.body
    console.log(Numbers)
    angle = Numbers['angle']

    res.send({"sin":sinx(angle), "cos":cosx(angle), "tan":tanx(angle),
    "sec":secx(angle), "cosec":cosecx(angle), "cot":cotx(angle)})
});

//Math-Log3 Calculator
api.post('/Q4/inverse_trig',(req,res) =>{   
    const Numbers = req.body
    console.log(Numbers)
    val = Numbers['value']

    res.send({"arcsin":arcsinx(val), "arccos":arccosx(val), "arctan":arctanx(val)})
});

// -------------------------Quest 4 END------------------------//


// -------------------------Question 5 ------------------------//


//to find length of an array
function array_length(arr){
    let length = 0;
    while(arr[length] != undefined){
        length++;
    }
    return length;
}


//calculate mean
function cal_mean(arr,size){
    var sum = 0.0;
    for(let i = 0;i < size; i++){
        sum += arr[i];
    }
    console.log(arr,size,sum)
    return sum/size;
}


function standard_deviation(arr){
    var size = array_length(arr);
    var mean = cal_mean(arr,size);
    console.log(size,mean);

    var numerator = 0;
    for(let i = 0 ;i < size ; i++){
        temp = (arr[i]-mean) ** 2;
        numerator = numerator + temp;
    }

    sd = ((numerator/(size-1)) ** (0.5))

    return sd;
}

function variance(arr){
    return ((standard_deviation(arr)) ** 2)
}

function linear_regression(ind,dep){
    var ind_size = array_length(ind);
    var ind_mean = cal_mean(ind,ind_size);

    var dep_size = array_length(dep);
    var dep_mean = cal_mean(dep,dep_size);

    if (ind_size != dep_size){
        console.log("Size varies")
        return "Size varies"
    }

    var numerator = 0.0;
    var denominator = 0.0;

    for(let i = 0 ; i < ind_size ; i++){
        temp = ind[i] - ind_mean;
        denominator = denominator + temp ** 2; 
        numerator = numerator + (temp * (dep[i] - dep_mean));
    }
    console.log(numerator,denominator)

    var y = dep_mean;
    var b1 = numerator/denominator;
    var b0 = dep_mean - (ind_mean*b1);
    console.log("y,b0,b1",y,b0,b1);
    out_str = "y = "+y+", b0 = "+b0+", b1 = "+b1;
    return(out_str)
}


//Statistics Calculator
api.post('/Q5/',(req,res) =>{   
    const request = req.body

    list1 = request['list1']
    list2 = request['list2']
    list3 = request['list3']

    res.send({"std_deviation":standard_deviation(list1), "variance":variance(list1), "linear_reg":linear_regression(list2, list3)})
});


// -------------------------Quest 5 END------------------------//
<?php
// -------------------------Question 1 ------------------------//


//Q1
function calc1($current, $voltage, $curr_unit, $volt_unit){

    $w = (($current * $voltage)/($curr_unit * $volt_unit));
    return ([w/1000, w, w*1000]);

} 



function calc2($power, $volt){
    
    $w = ($power[0] / $volt[0]) * ($power[1]  * $volt[1]);
    
    return ([$w, $w * 1000]);

}


// -------------------------Question 2 ------------------------//
define("LN10",2.3025850929940456840179914546844);

function natural_log($x){
    //var num ;
    $num = ($x - 1)/($x + 1);
    $sum = 0; 
    $old_sum = -1;
    for($i = 1 ; $sum != $old_sum ; $i++){
        $old_sum = $sum;
        $denomiator = (2*$i)-1;
        $output = ($num ** $denomiator)/$denomiator;
        $sum += $output;
        
    }
    return 2*$sum;
}


function common_log($x){
    if($x > 0){
        return (natural_log($x)/LN10);
    }
    return 0;
}


function anti_log($x,$base){
    if($x > 0){
        return ($base ** $x);
    }
    return 0;
}


// Test Cases
// echo natural_log(12)."\n";
// echo common_log(12)."\n";
// echo anti_log(1.07918124,10)."\n";


// -------------------------Question 3 ------------------------//


function GCF($num1,$num2) {
    if($num2 == 0){
        return $num1;
    }
    return GCF($num2,$num1 % $num2);
  }


function LCM($num1, $num2) {
    return (($num1 * $num2) / GCF($num1,$num2));
}

function sq_rt($num1) {
    return (($num1 ** (1/2)));
}

function cb_rt($num1) {
    return (($num1 ** (1/3)));
}

function n_rt($num1,$n) {
    return (($num1 ** (1/$n)));
}


// Test Cases
// echo GCF(10,20)."\n";
// echo LCM(10,20)."\n";
// echo sq_rt(3)."\n";
// echo cb_rt(729)."\n";
// echo n_rt(3,2)."\n";


// -------------------------Question 4 ------------------------//

define("PI", 3.14159);
define("TAYLOR_TERMS",10);
define("TAYLOR_TERMS_ARCTAN",50);


//factorial
function fact($number){
    return ($number <= 0 ) ? 1 : $number * fact ($number - 1);
}


function sinx($deg) {
    $deg %= 360; 
    $rad = $deg * PI / 180;
    $sin = 0;

    for( $i = 0; $i < TAYLOR_TERMS; $i++) { 
        $sin += ((-1) ** $i) * (($rad**(2 * $i + 1)) / fact(2 * $i + 1));
    }
    return $sin;
}

function cosx($deg) {
    $deg %= 360; 
    $rad = $deg * PI / 180;
    $cos = 0;


    for($i = 0; $i < TAYLOR_TERMS; $i++) { 
        $cos += ((-1) ** $i) * (($rad**(2 * $i )) / fact(2 * $i ));
    }
    return $cos;
}

function tanx($deg) {
    $deg %= 360; 
    if(( $deg == 90 || ($deg == 270))){
        return 'undefined';
    }
    return sinx($deg)/cosx($deg);
}

function secx($deg) {
    $deg %= 360; 
    if(( $deg == 90)|| ($deg == 270)){
        return 'undefined';
    }
    return 1/cosx($deg);
}

function cosecx($deg) {
    $deg %= 360; 
    if(( $deg == 0)|| ($deg == 180)){
        return 'undefined';
    }
    return 1/sinx($deg);
}

function cotx($deg) {
    $deg %= 360; 
    if(( $deg == 0) || ($deg == 180)){
        return 'undefined';
    }
    return cosx($deg)/sinx($deg);
}

function arcsinx($x) {
    $temp = $x/((1- ($x**2)) ** 0.5);
    return arctanx($temp);
}

function arccosx($x) {
    $temp = ((1- ($x**2)) ** 0.5)/$x;
    return arctanx($temp);
}

function arctanx($x) {
    $arctan = 0;
    for($i = 0; $i < TAYLOR_TERMS_ARCTAN; $i++) { 
        $arctan += ((-1) ** $i) * (($x**(2 * $i + 1)) / (2 * $i + 1));
    }
    return $arctan*57.2958;
}


// Test Cases
// echo sinx(32)."\n";
// echo cosx(23)."\n";
// echo tanx(90)."\n";
// echo cotx(89)."\n";
// echo secx(33)."\n";
// echo cosecx(227)."\n";
// echo arctanx(.2)."\n";
// echo arccosx(-0.3)."\n";
// echo arcsinx(.2)."\n";

// -------------------------Question 5 ------------------------//


function array_length($arr){
    $length = 0;
    foreach ($arr as $item) {
        $length++;
    }
    return $length;
}

function cal_mean($arr,$size){
    $sum = 0.0;
    for( $i = 0;$i < $size; $i++){
        $sum += $arr[$i];
    }
    return $sum/$size;
}

function standard_deviation($arr){
    $size = array_length($arr);
    $mean = cal_mean($arr,$size);


    $numerator = 0;
    for($i = 0 ;$i < $size ; $i++){
        $temp = ($arr[$i]-$mean) ** 2;
        $numerator = $numerator + $temp;
    }

    $sd = (($numerator/($size-1)) ** (0.5));

    return $sd;
}

function variance($arr){
    return ((standard_deviation($arr)) ** 2);
}

function linear_regression($ind,$dep){
    $ind_size = array_length($ind);
    $ind_mean = cal_mean($ind,$ind_size);

    $dep_size = array_length($dep);
    $dep_mean = cal_mean($dep,$dep_size);

    if ($ind_size != $dep_size){
        echo "Size varies";
        return "Size varies";
    }

    $numerator = 0.0;
    $denominator = 0.0;

    for( $i = 0 ; $i < $ind_size ; $i++){
        $temp = $ind[$i] - $ind_mean;
        $denominator = $denominator + $temp ** 2; 
        $numerator = $numerator + ($temp * ($dep[$i] - $dep_mean));
    }

    $y = $dep_mean;
    $b1 = $numerator/$denominator;
    $b0 = $dep_mean - ($ind_mean*$b1);
    $out_str = "y = ".$y.", b0 = ".$b0.", b1 = ".$b1;
    return($out_str);
}


// echo cal_mean([3,3,3],3);
// echo array_length([])."\n";
// echo standard_deviation([10, 12, 23, 23, 16, 23, 21, 16])."\n";
// echo variance([10, 12, 23, 23, 16, 23, 21, 16])."\n";
// echo linear_regression([10, 12,23,16,21],[45,56,100,70,90])."\n";


?>
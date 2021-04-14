# import library 
import math, random
  
# function to generate OTP 
def generateOTP() : 
  
    # Declare a string variable   
    # which stores all string  
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+_-='
    OTP = "" 

    length = len(string) 
    for i in range(random.randint(5,10)) : 
        OTP += string[math.floor(random.random() * length)] 
    
    return OTP

otp = generateOTP()
print(otp)
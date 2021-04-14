from captcha.image import ImageCaptcha
import base64
import random

def otp():
    otp = []
    for _ in range(6):
        r = random.choice([(48, 57), (65, 90)])
        otp.append(chr(random.randint(*r)))
    otp = "".join(otp)
    resp_data = {
        "OTP": otp 
    }
    return resp_data 

def captcha():
    img = ImageCaptcha()
    ans=otp()["OTP"]
    data = img.generate(ans)
    rv = base64.b64encode(data.getvalue()).decode()
    resp_data = {
        "captcha":rv,
        "answer":ans
    }
    return resp_data

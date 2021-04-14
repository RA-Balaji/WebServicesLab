
import clx.xms
import requests
import random
import math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
#918825855642


def generateOTP() : 
  
    # Declare a string variable   
    # which stores all string  
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+_-='
    OTP = "" 

    length = len(string) 
    for i in range(random.randint(5,10)) : 
        OTP += string[math.floor(random.random() * length)] 
    
    return OTP

global comn_otp
comn_otp = generateOTP()

def send_otp_mobile():
  client = clx.xms.Client(service_plan_id='7dbb615abf724082bfe34217efb937ea', token='e81b7a0c92224ebaa30b2dc9d2de215b')

  create = clx.xms.api.MtBatchTextSmsCreate()
  create.sender = '447537404817'
  create.recipients = {'918124198950'}
  create.body = comn_otp + " is the OTP"
  print(comn_otp + " in mobile")

  try:
    batch = client.create_batch(create)
  except (requests.exceptions.RequestException,
    clx.xms.exceptions.ApiException) as ex:
    print('Failed to communicate with XMS: %s' % str(ex))


def send_otp_mail(email):
    print(comn_otp + " in mail")
    #The mail addresses and password
    sender_address = 'otpbot.webservice@gmail.com'
    sender_pass = 'balaji1234'
    receiver_address = email

    #print(mail_content)
    #Setup the MIME
    message = MIMEMultipart()

    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] =  "OTP for Library Portal"  #The subject line
    #The body and the attachments for the mail

    mail_content = comn_otp + " is the OTP"
    message.attach(MIMEText(mail_content, 'plain'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()

    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def main_fun(email):
  send_otp_mobile()
  send_otp_mail(email)
  return comn_otp

#main_fun('balaji.balaji235@gmail.com')
#send_otp_mail()
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl

def send_mail(email):
    message_content = "Registration Link is: https://www.google.com"
    print(message_content + " in mail")
    #The mail addresses and password
    sender_address = 'otpbot.webservice@gmail.com'
    sender_pass = 'balaji1234'
    receiver_address = email

    #print(mail_content)
    #Setup the MIME
    message = MIMEMultipart()

    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] =  "Library Registration"  #The subject line
    #The body and the attachments for the mail
    print(type(message))
    mail_content = message_content + ' is the link'
    message.attach(MIMEText(mail_content, 'plain'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()

    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

#send_mail('balaji.balaji235@gmail.com', 'hello')
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

Sender_Email = "belaface.help@gmail.com"
Reciever_Email = "jibon.py@gmail.com"
Password = input('Enter your email account password: ')


def SendMail(ImgFileName):
    with open(ImgFileName, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'jibon.py@mail.com'
    msg['To'] = 'e@mail.cc'

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(Sender_Email, Password)
    s.sendmail(Sender_Email, Reciever_Email, msg.as_string())
    s.quit()


# import smtplib
# Sender_Email = "belaface.help@gmail.com"
# Reciever_Email = "jibon.py@gmail.com"
# Password = input('Enter your email account password: ')
#
# Subject = "Test Email from CodeItBro"
# Body = "Hi, hope you are doing fine! Stay Home! Stay Safe!"
# Message = f'Subject: {Subject}\n\n{Body}'
#
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#     smtp.login(Sender_Email, Password)
#     smtp.sendmail(Sender_Email, Reciever_Email, Message)
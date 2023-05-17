import pandas as pd
import smtplib
import imghdr
from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.message import EmailMessage
SenderAddress = "belaface.help@gmail.com"
password = "help355168"

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = EmailMessage()
msg["Subject"] = "Hello there"

# with open('sakib.jpg', 'rb') as fp:
#     img = MIMEImage(fp.read())
#     img.add_header('Content-Disposition', 'attachment', filename="example.jpg")
#     msg.attach(img)

files = [
    'jibon.jpeg'
]
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_alternative(file_type,  subtype=file_type, filename="jibon.jpeg")


body = "Subject: {}\n\n{}".format(msg, msg.as_string(), msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
import pandas as pd
import smtplib
import imghdr
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

files = [
    'jibon.jpeg', 'sakib.jpg'
]
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_alternative(file_type,  subtype=file_type)


body = "Subject: {}\n\n{}".format(msg, msg, msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()


# import os
# import smtplib
#
# # EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# # EMAIL_PASSWORD = os.environ.get('EMAIL_USER')
#
# SenderAddress = "belaface.help@gmail.com"
# password = "help355168"
#
# with smtplib.SMTP('localhost', 1025) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#
#     smtp.login(SenderAddress, password)
#     subject = "Hi"
#     body = "good"
#     msg = f'Subject: {subject}\n\n{body}'
#     smtp.sendmail(SenderAddress, 'jibon.py@gmail.com', msg)

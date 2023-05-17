import smtplib
import imghdr
from email.message import EmailMessage
import pandas as pd

Sender_Email = "belaface.help@gmail.com"
Password = "help355168"
newMessage = EmailMessage()
newMessage['Subject'] = "Hello there"
newMessage['From'] = Sender_Email
e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
newMessage['To'] = emails

newMessage.set_content('Thanks for believing in me')


files = ['My-Workstation.jpeg', 'sakib.jpg', 'belasea-offer.PNG']
for file in files:
    with open(file, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Sender_Email, Password)
    smtp.send_message(newMessage)

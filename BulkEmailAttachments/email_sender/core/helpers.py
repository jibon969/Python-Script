import smtplib
from email.message import EmailMessage
from django.conf import settings


def mail_client(reciever, subject, body, attachments=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL
    msg['To'] = reciever
    msg.set_content(body)
    if attachments:
        with attachments as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(settings.EMAIL, settings.EMAIL_PASSWORD)
        smtp.send_message(msg)

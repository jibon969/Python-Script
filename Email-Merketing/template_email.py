import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

gmail_user = input("Enter your email :");
gmail_password = input("Enter your password :");


# open the file in read mode
filename = open('Book1.csv', 'r')
# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
email = []

# values to empty list
for col in file:
    email.append(col['E-mail'])

receiver_email = email

msg = MIMEMultipart('related')
msg['Subject'] = "Offer Offer"
msg['From'] = gmail_user


html = """\
<div>


    <div style="margin: 20px; text-align: center;"> 
        <h3>৬৩% পর্যন্ত মেগা ডিসকাউন্ট অফার🥳 সেরা দামে স্কিন কেয়ার প্রোডাক্ট 😍</h3> <br> 
        <h3>বেলাসি-তে চলছে বিশাল ডিসকাউন্ট অফার! 🎉🎊</h3> <br> 
        <h3>🎀 ২২০০ টাকার Nature Republic SUPER AQUA MAX EX WATERY CREAM মাত্র ১০০০ টাকা</h3> <br> 
        <h3>🎀 ৭২০ টাকার Nature Republic FRESH HERB ACEROLA CLEANSING FOAM মাত্র ২৭৪ টাকা</h3> <br>  
        <h3>🎀 ১৫০ টাকার NATURE REPUBLIC REAL NATURE ROYAL JELLY MASK SHEET মাত্র ৭৪ টাকা</h3> <br>
        <div style= "text-align: center;"> <img src="cid:image1"> </div>
        <div style= "text-align: center;"> <img src="cid:image2"> </div>
        <div style= "text-align: center;"> <img src="cid:image3"> </div>
        <div style= "text-align: center;"> <img src="cid:image4"> </div>
        <h3>🎀 720 টাকার Innisfree Super Volcanic Pore Clay Mask মাত্র ২৯৪ টাকা</h3> <br> 
        <h3>আফার উপভোগ করতে এখনি রিপ্লাই করুন এই ইমেইল এ!👇</h3> <br> 
        <h3>*স্টক সীমিত‼️</h3> <br>
        <h3> You can also check our others offer at: <a href="https://belasea.com/products/product-offer/offer/">https://belasea.com/products/product-offer/offer/</a> </h3> <br>  
        <h3>Visit us : <a href="www.belasea.com">www.belasea.com </a> </h3> <br>
        <br>Thank You <br> BELASEA-BD</h3>

    </div>

</div>
"""
part2 = MIMEText(html, 'html')

msg.attach(part2)


fp = open('super-combo.jpeg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

fp = open('ordinary.jpeg', 'rb')
msgImage2 = MIMEImage(fp.read())
fp.close()

msgImage2.add_header('Content-ID', '<image2>')
msg.attach(msgImage2)


fp = open('vitamin-c.jpeg', 'rb')
msgImage3 = MIMEImage(fp.read())
fp.close()

msgImage3.add_header('Content-ID', '<image3>')
msg.attach(msgImage3)

fp = open('mac.jpeg', 'rb')
msgImage4 = MIMEImage(fp.read())
fp.close()

msgImage4.add_header('Content-ID', '<image4>')
msg.attach(msgImage4)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(gmail_user, gmail_password)
    for email in receiver_email:
      server.sendmail(gmail_user, email, msg.as_string()
    )
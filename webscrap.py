import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.ca/Professional-Ukulele-Mahogany-Rosewood-Beginner/dp/B07GQV4L3Y/ref=sr_1_1_sspa?crid=3FL6S3D99AVEJ&keywords=guitar&qid=1577756792&sprefix=gui%2Caps%2C181&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExV1IwQjA2UENSQUZHJmVuY3J5cHRlZElkPUEwOTUxOTMxMTdBTUhMOUU3MjNFTCZlbmNyeXB0ZWRBZElkPUEwNjE2MTA2MkdZQkZRRDJCWTVVRSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    sever.starttls() #incrypts connection
    server.ehlo()

    server.login('neelpatel3108.pn@gmail.com')
    subject = "Guiter Price Check"
    body = "Check the link! Price fell down from guiter. https://www.amazon.ca/Professional-Ukulele-Mahogany-Rosewood-Beginner/dp/B07GQV4L3Y/ref=sr_1_1_sspa?crid=3FL6S3D99AVEJ&keywords=guitar&qid=1577756792&sprefix=gui%2Caps%2C181&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExV1IwQjA2UENSQUZHJmVuY3J5cHRlZElkPUEwOTUxOTMxMTdBTUhMOUU3MjNFTCZlbmNyeXB0ZWRBZElkPUEwNjE2MTA2MkdZQkZRRDJCWTVVRSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'neelpatel3108.pn@gmail.com',
        'neelpatel98@hotmail.com',
        msg
    )
    server.quit()

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    convertedPrice = float(price[0:3])
    
 
    if(convertedPrice > 60):
        sendMail()

while(True):
    check_price()
    time.sleep(172800)
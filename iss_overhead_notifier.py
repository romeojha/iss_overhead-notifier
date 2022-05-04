#an program, when runned will rerun itself in 60 second to check the ISS satelite
#if its night and satelite location is near you, it will send you the mail
#to look up in the sky .
#a sms api, like twilio
#run on cloud
#hide the API tokens


from datetime import datetime
import requests
from webob import hour
import smtplib
import time

my_lat=28.436010
my_long=77.300006
email='rowmann33@gmail.com' #your email goes here
pas = "romeo848651"     #your password goes here
parameters={
    'formatted':0
}

request=requests.get('http://api.open-notify.org/iss-now.json')
request.raise_for_status()
response=request.json()
iss_latitude=float(response['iss_position']["latitude"])
iss_longitude=float(response['iss_position']["longitude"])
nows=datetime.now()
hour=nows.hour


def check_iss():
    if 19<hour<24:
        if abs(my_lat-iss_latitude)<1 and abs(my_long-iss_longitude)<1:
            print("iss near me")
            return True


while True:
    time.sleep(60)
    if check_iss()==True:
        mail=smtplib.SMTP("smtp.gmail.com")
        mail.starttls()
        mail.login(user=email,password=pas)
        mail.sendmail(
            to_addrs=email,
            from_addr=email,
            msg="subject: look up\n\n the iss satelite is overhead",
        )
        print('executed')
    else:
        print("none")

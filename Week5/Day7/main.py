import requests
import smtplib
import os

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "fa672cb3ae8e25ed3eb9531187d9be73"
LAT_VAL = 28.49
LONG_VAL = 76.994
MAIL_SERVER = "smtp.gmail.com"
SOURCE_EMAIL = "<Put your email id>"
PASSWORD = "<password>"
DESTINATION_EMAIL = "<destination email>"

def send_mail():
    with smtplib.SMTP("https://mail.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SOURCE_EMAIL,
                            to_addrs=DESTINATION_EMAIL,
                            msg=f"Subject: Bring Your Umbrella \n\n"
                                f"Its Going to rain today. Dont forget to bring your umbrella")


parameters = {
    "lat" : LAT_VAL,
    "lon" : LONG_VAL,
    "appid" : API_KEY,
    "cnt" : 4,
}

response = requests.get(URL, params=parameters)
response.raise_for_status()

data = response.json()

weather_data = [det["weather"][0]["id"] for det in data["list"]]
for info in weather_data:
    if info < 700:
        #send_mail()
        print("abcd")
        break


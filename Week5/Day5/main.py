import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
MAIL_SERVER = "smtp.gmail.com"
SOURCE_EMAIL = "<Put your email id>"
PASSWORD = "<password>"
DESTINATION_EMAIL = "<destination email>"

def is_iss_close(lati, long, sunst):
    if lati in range(MY_LAT-5, MY_LAT+5) and long in range(MY_LONG-5, MY_LONG+5) and time_now > sunset and time_now < sunrise:
        return True
    return False




while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if is_iss_close(iss_latitude, iss_longitude, sunset):
        with smtplib.SMTP(MAIL_SERVER) as connection:
            connection.starttls()
            connection.login(user=SOURCE_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=SOURCE_EMAIL, to_addrs=DESTINATION_EMAIL, msg="Subject: Look up\n\n LOOK UP")
    time.sleep(60)
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




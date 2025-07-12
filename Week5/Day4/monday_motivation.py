import datetime as dt
import smtplib
import random

MAIL_SERVER = "smtp.gmail.com"
SOURCE_EMAIL = "<Put your email id>"
PASSWORD = "<password>"
DESTINATION_EMAIL = "<destination email>"

with open("quotes.txt") as quote_file:
    quote_list = quote_file.readlines()
day_quote = random.choice(quote_list).strip("\n")

now = dt.datetime.now()
current_day = now.weekday()

if current_day==5:
    with smtplib.SMTP(MAIL_SERVER) as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs=DESTINATION_EMAIL,
                            from_addr=SOURCE_EMAIL,
                            msg=f"Subject: Quote of Saturday\n\n {day_quote}")



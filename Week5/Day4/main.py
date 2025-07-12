##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas as pd
import random

MAIL_SERVER = "smtp.gmail.com"
SOURCE_EMAIL = "<Put your email id>"
PASSWORD = "<password>"
DESTINATION_EMAIL = "<destination email>"

data = pd.read_csv("birthdays.csv").to_dict(orient="records")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

def read_random_template():
    wish_file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(wish_file, "r") as birthday_wish:
        letter_template = birthday_wish.read()
    return letter_template

connection = smtplib.SMTP(MAIL_SERVER)
connection.starttls()
connection.login(user=SOURCE_EMAIL, password=PASSWORD)

#Identify people who have birthday today and add them to the list
birthday_today_list = [data[index] for index in range(len(data)) if data[index]["month"] == current_month and data[index]["day"] == current_day]

#send birthday wishes to each person
for item in birthday_today_list:
    email_text = read_random_template().replace("[NAME]", item["name"])
    connection.sendmail(from_addr=SOURCE_EMAIL,
                        to_addrs=DESTINATION_EMAIL,
                        msg=f"Subject: Happy Birthday!!\n\n{email_text}")
connection.close()





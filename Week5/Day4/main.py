import smtplib
SOURCE_EMAIL = "<Put your email id>"
PASSWORD = "<password>"
DESTINATION_EMAIL = "<destination email>"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=SOURCE_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=SOURCE_EMAIL, to_addrs=DESTINATION_EMAIL, msg="Subject:Hello\n\n from me")
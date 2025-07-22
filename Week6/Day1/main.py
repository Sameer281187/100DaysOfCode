import requests
import smtplib
import os

STOCK_API_KEY = os.environ.get("AV_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK = "SDBL"
COMPANY_NAME = "Tesla"

MAIL_SERVER = "smtp.gmail.com"
SOURCE_EMAIL = "<Put your email id>"
PASSWORD = "<password>"
DESTINATION_EMAIL = "<destination email>"

def send_mail(content, change_direction, change):
    with smtplib.SMTP("https://mail.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SOURCE_EMAIL,
                            to_addrs=DESTINATION_EMAIL,
                            msg=f"Subject: {STOCK}: {change_direction} {change}\n\n"
                                f"{content}")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : f"{STOCK}.BSE",
    "outputsize" : "compact",
    "apikey" : STOCK_API_KEY,
}
url = "https://www.alphavantage.co/query"
response = requests.get(url, params=parameters)
response.raise_for_status()

data = response.json()
market_dates = data["Time Series (Daily)"].keys()
prev_day_close_price = float(data["Time Series (Daily)"][list(market_dates)[0]]["4. close"])
prior_to_prev_close_price = float(data["Time Series (Daily)"][list(market_dates)[1]]["4. close"])

percentage_change = 0
change_dir = None

if prev_day_close_price > prior_to_prev_close_price:
    percentage_change = (prev_day_close_price - prior_to_prev_close_price) * 100 / prior_to_prev_close_price
    change_dir = "🔺"
else:
    percentage_change = (prior_to_prev_close_price - prev_day_close_price) * 100 / prior_to_prev_close_price
    change_dir = "🔻"

if percentage_change > 1:
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
    }
    news_response = requests.get(news_url, params=news_params)
    news_response.raise_for_status()

    news_data = news_response.json()
    mail_content = ""

    for i in range(3):
        mail_content += (f"Headline: {news_data["articles"][i]["title"]}\n"
                         f"Brief: {news_data["articles"][i]["description"]}\n\n")

    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    send_mail(mail_content, change_dir, percentage_change)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


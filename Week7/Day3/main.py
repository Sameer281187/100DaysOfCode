from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
article_item = soup.select(".athing.submission span.titleline > a")
# article_text = article_item.text
# article_link =  article_item.get("href")
article_upvote = soup.select(".score")
article_details = []
max_val = 0
for i in range(len(article_item)):
    article = {
        "text": article_item[i].text,
        "link": article_item[i].get("href"),
        "upvotes": int(article_upvote[i].text.split(" ")[0])
    }
    article_details.append(article)

max_item = None
for item in article_details:
    if item["upvotes"] > max_val:
        max_val = item["upvotes"]
        max_item = item


print(max_item)
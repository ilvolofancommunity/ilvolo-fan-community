import json
import feedparser

feed = feedparser.parse("https://news.google.com/rss/search?q=IL+VOLO")

news = []

for item in feed.entries[:5]:
    news.append({
        "title": item.title,
        "date": item.published,
        "link": item.link,
        "image": ""
    })

with open("news.json", "w") as f:
    json.dump(news, f, indent=4)
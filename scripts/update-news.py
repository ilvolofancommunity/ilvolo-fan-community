import json
import feedparser

feed = feedparser.parse("https://news.google.com/rss/search?q=IL+VOLO")

news = []

for item in feed.entries[:6]:
    news.append({
        "title": item.title,
        "date": item.published,
        "summary": getattr(item, "summary", ""),
        "link": item.link,
        "image": ""
    })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, indent=4, ensure_ascii=False)
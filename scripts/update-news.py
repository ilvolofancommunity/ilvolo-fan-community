import json
import feedparser
from datetime import datetime

feed_url = "https://news.google.com/rss/search?q=IL+VOLO"

feed = feedparser.parse(feed_url)

news = []

for entry in feed.entries[:10]:
    news.append({
        "title": entry.title,
        "link": entry.link,
        "published": getattr(entry, "published", ""),
        "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, indent=4, ensure_ascii=False)

print(f"Updated {len(news)} news articles.")
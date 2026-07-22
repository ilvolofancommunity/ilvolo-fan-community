import json
import feedparser
import re
from email.utils import parsedate_to_datetime

feed = feedparser.parse(
    "https://news.google.com/rss/search?q=IL+VOLO&hl=en-US&gl=US&ceid=US:en"
)

print("Number of entries:", len(feed.entries))

news = []

entries = sorted(
    feed.entries,
    key=lambda x: parsedate_to_datetime(x.published),
    reverse=True
)

for item in entries[:6]:
    news.append({
        "title": item.title,
        "date": parsedate_to_datetime(item.published).strftime("%d %B %Y"),
        "summary": re.sub("<.*?>", "", getattr(item, "summary", ""))[:180] + "...",
        "link": item.link,
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Music_Notes.svg"
    })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, indent=4, ensure_ascii=False)
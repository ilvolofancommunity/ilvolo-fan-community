import json
from datetime import datetime

news_items = [
    {
        "title": "IL VOLO Latest Updates",
        "description": "Stay connected with the latest news, concerts and announcements from IL VOLO.",
        "date": datetime.now().strftime("%Y-%m-%d")
    }
]

with open("news.json", "w", encoding="utf-8") as file:
    json.dump(news_items, file, indent=4, ensure_ascii=False)

print("News updated successfully.")

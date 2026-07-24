import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.ilvolomusic.com/tour/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

with open("tour_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, "html.parser")

concerts = []

cards = soup.select("div.qodef-grid-item")

for card in cards:

    title = card.select_one(".qodef-e-title")
    date = card.select_one(".qodef-e-date")

    if not title or not date:
        continue

    concerts.append({
        "city": title.get_text(" ", strip=True),
        "date": date.get_text(" ", strip=True)
    })

with open("concerts.json", "w", encoding="utf-8") as f:
    json.dump(concerts, f, indent=4, ensure_ascii=False)

print(f"Saved {len(concerts)} concerts.")
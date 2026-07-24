import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.ilvolomusic.com/tour/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

MONTHS = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

response = requests.get(URL, headers=HEADERS, timeout=30)
response.raise_for_status()

with open("tour_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, "html.parser")

concerts = []
today = datetime.today().date()
cards = soup.select("div.qodef-grid-item")

for card in cards:

    title = card.select_one(".qodef-e-title")
    date_box = card.select_one(".qodef-e-date")

    if title is None or date_box is None:
        continue

    months = date_box.select(".qodef-e-month")
    day = date_box.select_one(".qodef-e-day")

    if len(months) < 2 or day is None:
        continue

    month_text = months[0].get_text(strip=True)[:3]
    year_text = months[1].get_text(strip=True)
    day_text = day.get_text(strip=True)

    if month_text not in MONTHS:
        continue

    try:
        event_date = datetime(
            int(year_text),
            MONTHS[month_text],
            int(day_text)
        ).date()
    except Exception:
        continue

    if event_date < today:
        continue

        city = title.get_text(" ", strip=True)

    venue = ""
    venue_tag = title.find("sup")

        if event_date < today:
        continue

    city = title.get_text(" ", strip=True)

    concerts.append({
        "event_date": event_date,
        "city": city,
        "venue": venue
    })

COUNTRIES = {
    "Este": "Italy",
    "Taormina": "Italy",
    "Rome": "Italy",
    "Florence": "Italy",
    "Milan": "Italy",
    "Turin": "Italy",
    "Bologna": "Italy",
    "Caserta": "Italy",
    "Barletta": "Italy",
    "Alghero": "Italy",
    "Macerata": "Italy",
    "Lanciano": "Italy",
    "Codroipo": "Italy",
    "Forte dei Marmi": "Italy",
    "Brescia": "Italy",
    "Thessaloniki": "Greece",
    "Corfu": "Greece"
}

final_concerts = []

for concert in sorted(concerts, key=lambda x: x["event_date"]):

    country = ""

    for city_name, country_name in COUNTRIES.items():
        if city_name.lower() in concert["city"].lower():
            country = country_name
            break

    final_concerts.append({
        "dateISO": concert["event_date"].strftime("%Y-%m-%d"),
        "date": concert["event_date"].strftime("%d %B %Y"),
        "city": concert["city"],
        "country": country,
        "venue": concert["venue"],
        "email": "mailto:ilvolomusic425@gmail.com",
        "telegram": "https://t.me/ilvolo_fan_community",
        "zangi": "https://zangi.com/dl/conversation/9402253010"
    })

with open("concerts.json", "w", encoding="utf-8") as f:
    json.dump(final_concerts, f, indent=4, ensure_ascii=False)

print(f"Saved {len(final_concerts)} concerts.")
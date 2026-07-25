import json
import re
import requests

from bs4 import BeautifulSoup
from datetime import datetime

# ==========================================================
# CONFIGURATION
# ==========================================================

URL = "https://www.ilvolomusic.com/tour/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}

EMAIL = "mailto:ilvolomusic425@gmail.com"
TELEGRAM = "https://t.me/ilvolo_fan_community"
ZANGI = "https://zangi.com/dl/conversation/9402253010"

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

COUNTRIES = {
    "Malaga": "Spain",
    "Murcia": "Spain",

    "Thessaloniki": "Greece",
    "Corfu": "Greece",

    "Este": "Italy",
    "Codroipo": "Italy",
    "Forte dei Marmi": "Italy",
    "Barletta": "Italy",
    "Alghero": "Italy",
    "Taormina": "Italy",
    "Lanciano": "Italy",
    "Macerata": "Italy",
    "Brescia": "Italy",
    "Caserta": "Italy",
    "Milan": "Italy",
    "Florence": "Italy",
    "Rome": "Italy",
    "Turin": "Italy",
    "Bologna": "Italy",
    "Cattolica": "Italy"
}
# ==========================================================
# HELPERS
# ==========================================================

def detect_country(city):

    for key, value in COUNTRIES.items():

        if key.lower() in city.lower():
            return value

    return ""


def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def download_page():

    print("Downloading official IL VOLO tour page...")

    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    print("Download complete.")

    return response.text


def save_html(html):

    with open(
        "tour_page.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)


# ==========================================================
# PARSE CONCERTS
# ==========================================================

def parse_concerts(html):

    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("div.qodef-e.qodef-grid-item")

    print(f"Found {len(cards)} concert cards.")

    # Temporary debug (Version 3)
    if cards:
        print("\n========== FIRST CONCERT HTML ==========\n")
        print(cards[0].prettify())
        print("\n========== END HTML ==========\n")

    concerts = []

    today = datetime.today().date()

    for card in cards:

        title = card.select_one(".qodef-e-title")
        date_box = card.select_one(".qodef-e-date")

        if title is None or date_box is None:
            continue

        months = date_box.select(".qodef-e-month")
        day = date_box.select_one(".qodef-e-day")

        if len(months) < 2 or day is None:
            continue

        month = months[0].get_text(strip=True)[:3]
        year = months[1].get_text(strip=True)

        try:
            day_number = int(day.get_text(strip=True))
        except ValueError:
            continue

        if month not in MONTHS:
            continue

        try:
            event_date = datetime(
                int(year),
                MONTHS[month],
                day_number
            ).date()
        except Exception:
            continue

        if event_date < today:
            continue

        full_title = clean_text(title.get_text(" ", strip=True))

        parts = full_title.split(" ", 2)

        city = full_title
        venue = ""

        if len(parts) >= 3:
            city = f"{parts[0]} {parts[1]}"
            venue = parts[2]

        city = clean_text(city)
        venue = clean_text(venue)

        concerts.append({
            "dateISO": event_date.strftime("%Y-%m-%d"),
            "date": event_date.strftime("%d %B %Y"),
            "city": city,
            "country": detect_country(city),
            "venue": venue,
            "email": EMAIL,
            "telegram": TELEGRAM,
            "zangi": ZANGI
        })

    return concerts


# ==========================================================
# SAVE JSON
# ==========================================================

def save_json(concerts):

    concerts = sorted(
        concerts,
        key=lambda x: x["dateISO"]
    )

    with open(
        "concerts.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            concerts,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved {len(concerts)} concerts.")


# ==========================================================
# MAIN
# ==========================================================

def main():

    html = download_page()

    save_html(html)

    concerts = parse_concerts(html)

    save_json(concerts)


if __name__ == "__main__":
    main()
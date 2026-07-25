import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.ilvolomusic.com/tour/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

EMAIL = "mailto:ilvolomusic425@gmail.com"
TELEGRAM = "https://t.me/ilvolo_fan_community"
ZANGI = "https://zangi.com/dl/conversation/9402253010"


def download_page():
    print("Downloading IL VOLO tour page...")

    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return response.text


def save_html(html):
    with open("tour_page.html", "w", encoding="utf-8") as f:
        f.write(html)


def main():
    html = download_page()
    save_html(html)

    soup = BeautifulSoup(html, "html.parser")

    print("Page downloaded successfully.")

    cards = soup.select("div.qodef-e.qodef-grid-item")

    print(f"Found {len(cards)} concert cards.")

    for i, card in enumerate(cards[:5], start=1):

        print("\n------------------")
        print(f"Concert {i}")
        print("------------------")

        print(card.get_text(" ", strip=True))


if __name__ == "__main__":
    main()
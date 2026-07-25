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

    concerts = []

    for card in cards:

        text = card.get_text(" ", strip=True)

        concerts.append({
            "raw": text
        })

    print(f"Collected {len(concerts)} concerts.")
print("\n========== FIRST 10 RAW CONCERTS ==========\n")

for i, concert in enumerate(concerts[:10], start=1):
    print(f"{i}. {concert['raw']}")

print("\n========== END ==========\n")
    with open("concerts_raw.json", "w", encoding="utf-8") as f:
        json.dump(concerts, f, indent=4, ensure_ascii=False)

    print("concerts_raw.json created.")


if __name__ == "__main__":
    main()
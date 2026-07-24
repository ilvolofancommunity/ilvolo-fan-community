import requests

URL = "https://www.ilvolomusic.com/tour/"

response = requests.get(
    URL,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

response.raise_for_status()

with open("tour_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("tour_page.html saved successfully.")
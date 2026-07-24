import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.ilvolomusic.com/tour/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("Official IL VOLO Tour page downloaded successfully.")
print("Page title:", soup.title.string if soup.title else "No title found")

with open("tour_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved page as tour_page.html")
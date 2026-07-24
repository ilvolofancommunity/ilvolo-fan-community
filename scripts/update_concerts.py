import requests
from bs4 import BeautifulSoup

URL = "https://www.ilvolomusic.com/tour/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

html = response.text

print("Length of page:", len(html))

print("\n========== FIRST 5000 CHARACTERS ==========\n")

print(html[:5000])
import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.ilvolomusic.com/tour/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

print("Downloaded official IL VOLO tour page.")
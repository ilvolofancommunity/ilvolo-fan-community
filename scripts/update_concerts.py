import requests
from bs4 import BeautifulSoup

URL = "https://www.ilvolomusic.com/tour/"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

classes = set()

for tag in soup.find_all(True):
    cls = tag.get("class")
    if cls:
        classes.update(cls)

print("========== CLASSES CONTAINING 'qodef' ==========")

for cls in sorted(classes):
    if "qodef" in cls.lower():
        print(cls)
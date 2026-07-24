import requests

URL = "https://www.ilvolomusic.com/tour/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

html = response.text

keywords = [
    "ESTE",
    "THESSALONIKI",
    "CORFU",
    "World Tour",
    "BUY VIP",
    "GIS"
]

for keyword in keywords:
    print(f"\nSearching for: {keyword}")
    index = html.upper().find(keyword.upper())

    if index == -1:
        print("Not found")
    else:
        start = max(0, index - 300)
        end = min(len(html), index + 800)
        print(html[start:end])
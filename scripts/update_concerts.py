import requests

html = requests.get(
    "https://www.ilvolomusic.com/tour/",
    headers={"User-Agent":"Mozilla/5.0"}
).text

keyword = "qodef-e-month"

index = html.find(keyword)

print(html[index-1000:index+4000])
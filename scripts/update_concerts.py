[
  {
    "city": "Malaga",
    "country": "Spain",
    "venue": "Plaza de Toros de la Malagueta",
    "date": "19 July 2026",
    "dateISO": "2026-07-19"
  },
  {
    "city": "Murcia",
    "country": "Spain",
    "venue": "Plaza de Toros",
    "date": "21 July 2026",
    "dateISO": "2026-07-21"
  },
  {
    "city": "Cattolica (RN)",
    "country": "Italy",
    "venue": "Arena Regina",
    "date": "23 July 2026",
    "dateISO": "2026-07-23"
  },
  {
    "city": "Este (PD)",
    "country": "Italy",
    "venue": "Este Music Festival - Castello Carrarese",
    "date": "25 July 2026",
    "dateISO": "2026-07-25"
  },
  {
    "city": "Thessaloniki",
    "country": "Greece",
    "venue": "City Theatre Gis",
    "date": "27 July 2026",
    "dateISO": "2026-07-27"
  },
  {
    "city": "Corfu",
    "country": "Greece",
    "venue": "Church St. George (Old Fortress)",
    "date": "29 July 2026",
    "dateISO": "2026-07-29"
  },
  {
    "city": "Codroipo (UD)",
    "country": "Italy",
    "venue": "Villa Manin",
    "date": "31 July 2026",
    "dateISO": "2026-07-31"
  },
  {
    "city": "Forte dei Marmi (LU)",
    "country": "Italy",
    "venue": "Villa Bertelli Live",
    "date": "02 August 2026",
    "dateISO": "2026-08-02"
  },
  {
    "city": "Barletta (BT)",
    "country": "Italy",
    "venue": "Fossato del Castello",
    "date": "07 August 2026",
    "dateISO": "2026-08-07"
  },
  {
    "city": "Alghero (SS)",
    "country": "Italy",
    "venue": "Anfiteatro Ivan Graziani - Alguer Summer Festival",
    "date": "09 August 2026",
    "dateISO": "2026-08-09"
  },
  {
    "city": "Taormina (ME)",
    "country": "Italy",
    "venue": "Teatro Antico",
    "date": "22 August 2026",
    "dateISO": "2026-08-22"
  },
  {
    "city": "Taormina (ME)",
    "country": "Italy",
    "venue": "Teatro Antico",
    "date": "23 August 2026",
    "dateISO": "2026-08-23"
  },
  {
    "city": "Lanciano (CH)",
    "country": "Italy",
    "venue": "Parco Villa delle Rose",
    "date": "27 August 2026",
    "dateISO": "2026-08-27"
  },
  {
    "city": "Macerata (MC)",
    "country": "Italy",
    "venue": "Sferisterio",
    "date": "28 August 2026",
    "dateISO": "2026-08-28"
  },
  {
    "city": "Brescia (BS)",
    "country": "Italy",
    "venue": "Piazza della Loggia",
    "date": "06 September 2026",
    "dateISO": "2026-09-06"
  },
  {
    "city": "Caserta (CE)",
    "country": "Italy",
    "venue": "Reggia di Caserta",
    "date": "08 September 2026",
    "dateISO": "2026-09-08"
  }

,
{
  "city": "Milan",
  "country": "Italy",
  "venue": "Unipol Forum",
  "date": "07 December 2026",
  "dateISO": "2026-12-07"
},
{
  "city": "Florence",
  "country": "Italy",
  "venue": "Nelson Mandela Forum",
  "date": "12 December 2026",
  "dateISO": "2026-12-12"
},
{
  "city": "Rome",
  "country": "Italy",
  "venue": "Palazzo dello Sport",
  "date": "17 December 2026",
  "dateISO": "2026-12-17"
},
{
  "city": "Turin",
  "country": "Italy",
  "venue": "Inalpi Arena",
  "date": "19 December 2026",
  "dateISO": "2026-12-19"
},
{
  "city": "Bologna",
  "country": "Italy",
  "venue": "Unipol Arena",
  "date": "20 December 2026",
  "dateISO": "2026-12-20"
}

# Find all possible concert cards
cards = soup.select("div.qodef-grid-item")

for card in cards:

    title = card.select_one(".qodef-e-title")
    date_box = card.select_one(".qodef-e-date")

    if not title or not date_box:
        continue

    months = date_box.select(".qodef-e-month")
    day = date_box.select_one(".qodef-e-day")

    if len(months) < 2 or day is None:
        continue

    month_name = months[0].get_text(strip=True)[:3]
    year_text = months[1].get_text(strip=True)
    day_text = day.get_text(strip=True)

    if month_name not in MONTHS:
        continue

    try:
        event_date = datetime(
            int(year_text),
            MONTHS[month_name],
            int(day_text)
        ).date()
    except Exception:
        continue

    # Ignore concerts that have already passed
    if event_date < today:
        continue

    city = title.get_text(" ", strip=True)

    venue = ""
    venue_tag = title.find("sup")
    if venue_tag:
        venue = venue_tag.get_text(" ", strip=True)
        city = city.replace(venue, "").strip()

    concerts.append({
        "event_date": event_date,
        "city": city,
        "venue": venue
    })

COUNTRIES = {
    "Este": "Italy",
    "Taormina": "Italy",
    "Rome": "Italy",
    "Verona": "Italy",
    "Florence": "Italy",
    "Thessaloniki": "Greece",
    "Corfu": "Greece",
    "Athens": "Greece",
    "Sofia": "Bulgaria",
    "Plovdiv": "Bulgaria",
    "Bucharest": "Romania",
    "Cluj": "Romania",
    "Warsaw": "Poland",
    "Krakow": "Poland",
    "Prague": "Czech Republic",
    "Bratislava": "Slovakia",
    "Budapest": "Hungary",
    "Zagreb": "Croatia",
    "Ljubljana": "Slovenia",
    "Vienna": "Austria",
    "Munich": "Germany",
    "Berlin": "Germany",
    "Paris": "France",
    "Madrid": "Spain",
    "Barcelona": "Spain",
    "Lisbon": "Portugal",
    "London": "United Kingdom",
    "Dublin": "Ireland"
}

final_concerts = []

for concert in sorted(concerts, key=lambda x: x["event_date"]):

    country = ""

    for city_name, country_name in COUNTRIES.items():
        if city_name.lower() in concert["city"].lower():
            country = country_name
            break

    final_concerts.append({
        "dateISO": concert["event_date"].strftime("%Y-%m-%d"),
        "date": concert["event_date"].strftime("%d %B %Y"),
        "city": concert["city"],
        "country": country,
        "venue": concert["venue"],
        "email": "mailto:ilvolomusic425@gmail.com",
        "telegram": "https://t.me/ilvolo_fan_community",
        "zangi": "https://zangi.com/dl/conversation/9402253010"
    })

with open("concerts.json", "w", encoding="utf-8") as f:
    json.dump(final_concerts, f, indent=4, ensure_ascii=False)

print(f"Saved {len(final_concerts)} concerts.")

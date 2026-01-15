import json
import pandas as pd
from datetime import datetime

RAW_FILE_PATH = "data/raw/weather_raw.json"

with open(RAW_FILE_PATH, "r") as file:
    raw_data = json.load(file)

rows = []

for item in raw_data:
    row = {
        "city": item["city"],
        "fetched_at": item["fetched_at"],
        "temperature_c": round(item["main"]["temp"] - 273.15, 2),
        "humidity": item["main"]["humidity"],
        "pressure": item["main"]["pressure"],
        "wind_speed": item["wind"]["speed"],
        "weather_main": item["weather"][0]["main"],
        "weather_description": item["weather"][0]["description"],
        "timestamp": datetime.fromtimestamp(item["dt"])
    }
    rows.append(row)

df = pd.DataFrame(rows)

OUTPUT_FILE_PATH = "data/processed/weather_clean.csv"
df.to_csv(OUTPUT_FILE_PATH, index=False)

print("Cleaned data for multiple cities saved successfully!")
print(df)

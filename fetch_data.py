import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# 🔹 Cities to fetch
CITIES = ["Mumbai", "Delhi", "Bangalore"]

all_weather_data = []

for city in CITIES:
    params = {
        "q": city,
        "appid": API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print(f"Failed to fetch data for {city}")
        continue

    data = response.json()
    data["city"] = city
    data["fetched_at"] = datetime.now().isoformat()

    all_weather_data.append(data)

# Save all city data
output_path = "data/raw/weather_raw.json"
with open(output_path, "w") as file:
    json.dump(all_weather_data, file, indent=4)

print("Weather data for multiple cities saved successfully!")

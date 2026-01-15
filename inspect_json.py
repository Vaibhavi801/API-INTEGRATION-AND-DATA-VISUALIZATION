import json

with open("data/raw/weather_raw.json", "r") as file:
    data = json.load(file)

print(data.keys())
print(data["main"].keys())
print(data["weather"][0])

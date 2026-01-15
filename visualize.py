import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_PATH = "data/processed/weather_clean.csv"
df = pd.read_csv(DATA_PATH)

print(df)

OUTPUT_DIR = "outputs/plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.figure()
sns.barplot(
    x="city",
    y="temperature_c",
    data=df
)

plt.title("Temperature (°C) by City")
plt.ylabel("Temperature (°C)")
plt.xlabel("City")

plt.savefig(f"{OUTPUT_DIR}/temperature.png")
plt.close()

plt.figure()
sns.barplot(
    x="city",
    y="wind_speed",
    data=df
)

plt.title("Wind Speed (m/s) by City")
plt.ylabel("Wind Speed (m/s)")
plt.xlabel("City")

plt.savefig(f"{OUTPUT_DIR}/wind_speed.png")
plt.close()


plt.figure()
sns.barplot(x="city", y="humidity", data=df)

plt.title("Humidity (%) by City")
plt.ylabel("Humidity (%)")
plt.xlabel("City")

plt.savefig(f"{OUTPUT_DIR}/humidity.png")
plt.close()

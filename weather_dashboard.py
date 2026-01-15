import matplotlib
matplotlib.use("Agg")  # Non-GUI backend (fixes Tcl/Tk issue)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_PATH = "data/processed/weather_clean.csv"
df = pd.read_csv(DATA_PATH)

OUTPUT_DIR = "outputs/plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
sns.barplot(
    x="city",
    y="temperature_c",
    hue="city",
    data=df,
    palette="Set2",
    legend=False
)
plt.title("Temperature (°C)")
plt.ylabel("°C")
plt.xlabel("")

plt.subplot(3, 1, 2)
sns.barplot(
    x="city",
    y="humidity",
    hue="city",
    data=df,
    palette="Set2",
    legend=False
)
plt.title("Humidity (%)")
plt.ylabel("%")
plt.xlabel("")

plt.subplot(3, 1, 3)
sns.barplot(
    x="city",
    y="wind_speed",
    hue="city",
    data=df,
    palette="Set2",
    legend=False
)
plt.title("Wind Speed (m/s)")
plt.ylabel("m/s")
plt.xlabel("City")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/weather_dashboard.png")
plt.close()

print("Weather dashboard created successfully!")

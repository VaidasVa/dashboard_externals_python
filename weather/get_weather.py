import json
import os

import requests
from dotenv import load_dotenv

from weather.get_geo import get_geo

load_dotenv()

endpoint = os.getenv("ENDPOINT")
api = os.getenv("OPENWEATHER_API_KEY")
print(api)
exclude = "minutely,hourly,alerts"
lat = get_geo()[0]
lon = get_geo()[1]


def get_current_weather():
    url = f"{endpoint}data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={api}"
    current_weather_response = requests.get(url).json()
    city = current_weather_response["name"]
    temperature = current_weather_response['main']['temp']
    icon = current_weather_response['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    response = {"city": city, "temperature": temperature, "iconUrl": icon_url}
    return json.dumps(response)


get_current_weather()
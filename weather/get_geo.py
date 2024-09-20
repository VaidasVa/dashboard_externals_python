import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

city = "Vilnius"
state = ""
country = "LT"
limit = 1
api = os.getenv("OPENWEATHER_API_KEY")
geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={api}"


def get_geo():
    response = requests.get(geo)
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        return json.dumps({"lat": data[0]['lat'], "lon": data[0]['lon']})
    else:
        return json.dumps({"lat": "54.6870458", "lon": "25.2829111"})

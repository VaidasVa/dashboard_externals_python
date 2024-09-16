import os
import requests

from dotenv import load_dotenv

load_dotenv()

city = "Vilnius"
state = ""
country = "LT"
limit = 1
api = os.getenv("OPENWEATHER_API_KEY")
print(api)
geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={api}"
print(geo)

def get_geo():
    response = requests.get(geo)
    return response.json()[0]['lat'], response.json()[0]['lon']

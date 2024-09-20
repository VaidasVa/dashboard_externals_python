
from flask import Blueprint

from weather import get_weather

weather_bp = Blueprint('weather', __name__)


@weather_bp.route("/api/v1/getCurrentWeather", methods=["GET"])
def get_current_weather():
    response = get_weather.get_current_weather()
    return response

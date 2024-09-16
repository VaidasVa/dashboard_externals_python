from flask import Flask
from flask_cors import CORS, cross_origin

import weather.get_weather

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://localhost:5173"])


@app.route("/api/v1/getCurrentWeather", methods=["GET"])
def get_current_weather():
    response = weather.get_weather.get_current_weather()
    return response


if __name__ == '__main__':
    app.run(debug=False)

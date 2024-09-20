from flask import Flask
from flask_cors import CORS

from web.news_feed_controller import news_bp
from web.weather_controller import weather_bp


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:4173"])
app.register_blueprint(weather_bp)
app.register_blueprint(news_bp)

if __name__ == '__main__':
    app.run()

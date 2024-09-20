from flask import Flask
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

from web.news_feed_controller import news_bp
from web.weather_controller import weather_bp


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:4173",
                   "http://192.168.50.50:3000", "http://192.168.50.50:4173", "http://192.168.50.50:5173",
                   "http://78.157.75.237:5173", "http://78.157.75.237"])
app.register_blueprint(weather_bp)
app.register_blueprint(news_bp)

if __name__ == '__main__':
    http_server = WSGIServer(('', 5050), app)
    http_server.serve_forever()
    app.run()

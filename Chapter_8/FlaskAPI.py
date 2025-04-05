from flask import Flask, jsonify
import requests, os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

API_KEY_WEATHER = os.getenv("API_KEY_WEATHER")
City = "Hue"
Url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY_WEATHER}"

info = {
    "Temperature": 0,
    "Humidity": 0,
    "Wind Speed": 0,
    "Main": ""
}

def get_weather_api():
    response = requests.get(Url)
    data = response.json()
    info["Temperature"] = str(round((data["main"]["temp"] - 273.15), 2)) + " Celsius" 
    info["Humidity"] = str(data["main"]["humidity"]) + "%"
    info["Wind Speed"] = str(data["wind"]["speed"]) + " m/s"
    info["Main"] = data["weather"][0]["main"]

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/api/weather')
def get_weather():
    get_weather_api()
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)


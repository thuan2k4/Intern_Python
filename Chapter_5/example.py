import requests, os, json
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()

API_KEY_WEATHER = os.getenv("API_KEY_WEATHER")
City = "Hue"
Url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={API_KEY_WEATHER}"
info = {
    "Temperature": 0,
    "Humidity": 0,
    "Wind Speed": 0,
    "Main": ""
}

response = requests.get(Url)
data = response.json()
# print(type(data))
# pprint(data, indent=4)

def get_weather(data):
    info["Temperature"] = str(round((data["main"]["temp"] - 273.15), 2)) + " Celsius" 
    info["Humidity"] = str(data["main"]["humidity"]) + "%"
    info["Wind Speed"] = str(data["wind"]["speed"]) + " m/s"
    info["Main"] = data["weather"][0]["main"]

get_weather(data)
print(info)

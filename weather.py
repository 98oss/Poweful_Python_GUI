import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("api_key")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_current_weather(location):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
        respone = requests.get(url)
        respone.raise_for_status()
        data = respone.json()

        weather_info ={
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_info
    except requests.exceptions.RequestException as e:
        return{"error": f"Error fetching weather data: {e}"}
    
def get_forecast(location, days=7):
    try:
        url = f"{BASE_URL}?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        forecast_info = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return forecast_info
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching forecast data: {e}"}
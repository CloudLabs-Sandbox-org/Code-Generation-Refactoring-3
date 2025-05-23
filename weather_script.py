# Fetch weather data from OpenWeatherMap API
import requests
import json
import os
from datetime import datetime, timedelta
import pytz
import logging
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)   
# Get API key from environment variable
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
if not API_KEY:
    logger.error("API key not found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
    exit(1)
# Define the base URL for the OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ...existing code...

def display_weather_info(data):
    """
    Process and display weather information such as temperature, humidity, and weather conditions.
    """
    if not data:
        logger.error("No data to display.")
        return

    city = data.get('name')
    main = data.get('main', {})
    weather = data.get('weather', [{}])[0]
    temp = main.get('temp')
    humidity = main.get('humidity')
    condition = weather.get('description', 'N/A').title()

    print(f"Weather in {city}:")
    print(f"  Temperature: {temp}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Condition: {condition}")

# Define the function to fetch weather data
def fetch_weather_data(city):
    try:
        # Construct the full API URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        # Make the API request
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            logger.error(f"Error fetching data from OpenWeatherMap: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None
        
if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(city)
    display_weather_info(weather_data)
#!/usr/bin/python

import requests
from weather_key import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Get weather information for the specified city."""
    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        # Access temperature in Celsius
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15

        # Access weather description
        weather_description = data['weather'][0]['description']
        
        print(f'Weather in {city}: {weather_description}')
        print(f'Temperature in {city}: {temperature_celsius:.2f}°C')
    else:
        print(f"An error occurred: {response.status_code}")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)

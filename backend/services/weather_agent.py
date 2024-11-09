import requests
from backend.utils.city_coordinates import get_city_coordinates

def get_weather(city_name, date):
    # Fetch city coordinates
    coordinates = get_city_coordinates(city_name)
    lat = coordinates['latitude']
    lon = coordinates['longitude']
    
    # Define the API URL for weather data
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()

    # Check for the hourly forecast data
    if 'hourly' in data:
        try:
            # Extract the latest temperature and wind speed values
            latest_temperature = data['hourly']['temperature_2m'][0]
            latest_wind_speed = data['hourly']['wind_speed_10m'][0]
            return f"Temperature: {latest_temperature}°C, Wind Speed: {latest_wind_speed} km/h"
        except (KeyError, IndexError) as e:
            return "Weather data not available"
    else:
        return "Weather data not available"

# def get_weather(city_name, date):
#     coordinates = get_city_coordinates(city_name)
#     lat = coordinates['latitude']
#     lon = coordinates['longitude']
#     print(lat, lon, "\n\n\n")
#     url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
#     response = requests.get(url)
#     data = response.json()
    
#     if 'current_weather' in data:
#         try:
#             temperature = data['current_weather']['temperature']
#             wind_speed = data['current_weather']['windspeed']
#             return f"Temperature: {temperature}°C, Wind Speed: {wind_speed} km/h"
#         except (KeyError, IndexError) as e:
#             return "Weather data not available"
#     else:
#         return "Weather data not available"


# import requests

# def get_weather(city, date):
#     api_key = "your_api_key"
#     url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&dt={date}"
#     response = requests.get(url)
#     data = response.json()
#     return data['forecast']['forecastday'][0]['day']['condition']['text']

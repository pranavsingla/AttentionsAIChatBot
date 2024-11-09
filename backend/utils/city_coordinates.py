from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# Initialize the geolocator with a custom User-Agent
geolocator = Nominatim(user_agent="your_unique_app_name_here")

def get_city_coordinates(city_name):
    try:
        location = geolocator.geocode(city_name, exactly_one=True, timeout=10)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude}
        else:
            print(f"Could not find coordinates for '{city_name}'. Returning approximate coordinates.")
            return {"latitude": 0.0, "longitude": 0.0}  # Default if not found
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Error with geocoding service: {e}. Returning default coordinates.")
        return {"latitude": 0.0, "longitude": 0.0}



# def get_city_coordinates(city_name):
#     geolocator = Nominatim(user_agent="geoapiExercises")  # Setting a user-agent is required
#     try:
#         location = geolocator.geocode(city_name, exactly_one=True, timeout=10)
#         if location:
#             return {"latitude": location.latitude, "longitude": location.longitude}
#         else:
#             print(f"Could not find coordinates for {city_name}")
#             return {"latitude": 0.0, "longitude": 0.0}
#     except GeocoderTimedOut:
#         print("Geocoding service timed out.")
#         return {"latitude": 0.0, "longitude": 0.0}

# city_coordinates = {
#     "Berlin": {"latitude": 52.5200, "longitude": 13.4050},
#     "London": {"latitude": 51.5074, "longitude": -0.1278},
#     "New York": {"latitude": 40.7128, "longitude": -74.0060},
#     "Tokyo": {"latitude": 35.6895, "longitude": 139.6917},
#     "Paris": {"latitude": 48.8566, "longitude": 2.3522},
#     # Add more cities as needed
# }

# def get_city_coordinates(city_name):
#     return city_coordinates.get(city_name, {"latitude": 0.0, "longitude": 0.0})  # Return (0,0) if city not found

from pydantic import BaseModel

class Preferences(BaseModel):
    city: str
    start_time: str
    end_time: str
    budget: float
    interests: list

class Itinerary(BaseModel):
    start_point: str
    places: list
    distances: list
    travel_times: list
    status: list
    lunch_spot: str
    weather: str
    map_url: str

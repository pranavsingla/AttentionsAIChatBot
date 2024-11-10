from pydantic import BaseModel
from typing import List, Optional

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

class User(BaseModel):
    username: str
    password: str  # Later can be replaced with hash passwords in a real app
    email: Optional[str] = None
    history: Optional[List[dict]] = []  # Store user's itinerary history here

class ItineraryRequest(BaseModel):
    username: str
    preferences: Preferences
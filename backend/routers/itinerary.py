from fastapi import APIRouter, HTTPException
from backend.models import Itinerary, Preferences, User, ItineraryRequest
from backend.services import llm_agent, optimization_agent, weather_agent, news_agent
from backend.routers.auth import db  # Import the singleton instance


router = APIRouter()


@router.post("/generate_itinerary")
def generate_itinerary(request: ItineraryRequest):
    username = request.username
    preferences = request.preferences
# def generate_itinerary(username: str, preferences: Preferences):
    # Check if user exists
    user = db.query("MATCH (u:User {username: $username}) RETURN u", {"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate itinerary
    llm = llm_agent.LLM()
    itinerary = llm.generate_itinerary(preferences)
    print(itinerary)
    optimized_itinerary = optimization_agent.optimize_itinerary(itinerary, preferences.budget)
    weather = weather_agent.get_weather(preferences.city, preferences.start_time)
    news = news_agent.get_news(preferences.city, preferences.start_time)

    final_itinerary = {
        "itinerary": optimized_itinerary,
        "weather": weather,
        "news": news
    }

    # Save itinerary history in Neo4j
    db.save_itinerary(username, final_itinerary)
    return final_itinerary


# @router.post("/generate_itinerary")
# def generate_itinerary(username: str, preferences: Preferences):
#     user = users_db.get(username)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     llm = llm_agent.LLM()
#     itinerary = llm.generate_itinerary(preferences)
#     optimized_itinerary = optimization_agent.optimize_itinerary(itinerary, preferences.budget)
#     weather = weather_agent.get_weather(preferences.city, preferences.start_time)
#     news = news_agent.get_news(preferences.city, preferences.start_time)

#     final_itinerary = {
#         "itinerary": optimized_itinerary,
#         "weather": weather,
#         "news": news
#     }

#     # Save the itinerary to user's history
#     user.history.append(final_itinerary)
#     return final_itinerary


# @router.post("/generate_itinerary")
# def generate_itinerary(preferences: Preferences):
#     llm = llm_agent.LLM()
#     itinerary = llm.generate_itinerary(preferences)
    
#     optimized_itinerary = optimization_agent.optimize_itinerary(itinerary, preferences.budget)
#     weather = weather_agent.get_weather(preferences.city, preferences.start_time)
#     news = news_agent.get_news(preferences.city, preferences.start_time)
    
#     final_itinerary = {
#         "itinerary": optimized_itinerary,
#         "weather": weather,
#         "news": news
#     }
    
#     return final_itinerary

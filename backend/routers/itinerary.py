from fastapi import APIRouter
from backend.models import Itinerary, Preferences
from backend.services import llm_agent, optimization_agent, weather_agent, news_agent

router = APIRouter()

@router.post("/generate_itinerary")
def generate_itinerary(preferences: Preferences):
    llm = llm_agent.LLM()
    itinerary = llm.generate_itinerary(preferences)
    
    optimized_itinerary = optimization_agent.optimize_itinerary(itinerary, preferences.budget)
    weather = weather_agent.get_weather(preferences.city, preferences.start_time)
    news = news_agent.get_news(preferences.city, preferences.start_time)
    
    final_itinerary = {
        "itinerary": optimized_itinerary,
        "weather": weather,
        "news": news
    }
    
    return final_itinerary

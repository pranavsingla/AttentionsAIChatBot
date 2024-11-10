from fastapi import FastAPI
from backend.routers import itinerary, preferences, auth
from backend.services.llm_agent import LLM

app = FastAPI()

# llm_instance = LLM() 
# @app.on_event("startup") 
# async def startup_event(): 
#     llm_instance.load_model() # Preload the model during startup

app.include_router(itinerary.router)
app.include_router(preferences.router)
app.include_router(auth.router)  # Include auth router

@app.get("/")
def read_root():
    return {"message": "Welcome to the One-Day Tour Planning API!"}

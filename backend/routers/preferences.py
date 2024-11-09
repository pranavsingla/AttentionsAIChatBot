from fastapi import APIRouter
from backend.models import Preferences
from backend.utils.db import Neo4jConnection

router = APIRouter()

@router.post("/set_preferences")
def set_preferences(preferences: Preferences):
    conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="password")
    query = """
    MERGE (p:Preferences {city: $city, start_time: $start_time, end_time: $end_time, budget: $budget})
    SET p.interests = $interests
    """
    conn.query(query, parameters=preferences.dict())
    conn.close()
    return {"status": "Preferences saved"}

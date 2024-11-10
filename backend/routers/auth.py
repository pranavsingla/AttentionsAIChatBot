from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import hashlib

router = APIRouter()

# In-memory storage for users (username -> password_hash)
users_db = {}

# Hash password before storing
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# Pydantic models for the requests
class User(BaseModel):
    username: str
    password: str

# Signup endpoint
@router.post("/signup")
def signup(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already taken")
    users_db[user.username] = hash_password(user.password)
    return {"message": "User created successfully!"}

# Login endpoint
@router.post("/login")
def login(user: User):
    stored_password_hash = users_db.get(user.username)
    if stored_password_hash is None:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if stored_password_hash != hash_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return {"message": "Login successful!"}

from fastapi import APIRouter, HTTPException, Depends
from backend.models import User
from database.init_db import Neo4jConnection
import hashlib

router = APIRouter()

# Initialize the database connection
# db = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", pwd="my_password")
# In-memory user storage for simplicity (Can replace this with a DB later)
db = users_db = {}

@router.post("/signup")
async def signup(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    # You can use a hashed password in real applications
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    users_db[user.username] = {"password": hashed_password, "email": user.email, "history": user.history}
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: User):
    stored_user = users_db.get(user.username)
    
    if not stored_user:
        raise HTTPException(status_code=400, detail="Username not found")
    
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    
    if hashed_password != stored_user["password"]:
        raise HTTPException(status_code=400, detail="Invalid password")
    
    return {"message": "Login successful"}

# @router.post("/signup")
# def signup(user: User):
#     # Check if the user already exists
#     if db.query("MATCH (u:User {username: $username}) RETURN u", {"username": user.username}):
#         raise HTTPException(status_code=400, detail="Username already exists")
#     # Create the user in the database
#     db.create_user(user.username, user.password, user.email)
#     return {"message": "User created successfully"}

# @router.post("/login")
# def login(username: str, password: str):
#     user = db.authenticate_user(username, password)
#     if not user:
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     return {"message": "Login successful", "username": username}


# from fastapi import APIRouter, HTTPException
# from backend.models import User

# router = APIRouter()
# users_db = {}  # Will be replaced with an actual database in production

# @router.post("/signup")
# def signup(user: User):
#     if user.username in users_db:
#         raise HTTPException(status_code=400, detail="Username already exists")
#     users_db[user.username] = user
#     return {"message": "User created successfully"}

# @router.post("/login")
# def login(username: str, password: str):
#     user = users_db.get(username)
#     if not user or user.password != password:
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     return {"message": "Login successful", "username": username}

from fastapi import APIRouter
from pydantic import BaseModel
import json
import os

router = APIRouter()

USERS_FILE = "users.json"

class RegisterUser(BaseModel):
    name: str
    phone: str
    domain: str
    experience: int
    preferred_location: str

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

@router.post("/register")
def register_user(user: RegisterUser):
    users = load_users()
    
    # Avoid duplicate phone numbers
    if any(u["phone"] == user.phone for u in users):
        return {"message": "User already registered."}
    
    users.append(user.dict())
    save_users(users)
    return {"message": "User registered successfully."}

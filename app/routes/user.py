from fastapi import APIRouter
from app.models.user import User
import json
import os
from app.database.data import USERS_DB
router = APIRouter()

USER_FILE = "user_data.json"

@router.post("/register")
def register_user(user: User):
    # Load existing
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            users = json.load(f)
    else:
        users = []

    # Append new user
    users.append(user.dict())

    # Save
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return {"message": f"User {user.name} registered successfully"}


from app.services.whatsapp_sender import send_whatsapp
from fastapi import APIRouter
from app.services.jsearch_fetcher import fetch_jobs  # ✅ this must return job list
from app.services.whatsapp_sender import send_whatsapp

router = APIRouter()

@router.get("/send-test-alert")
def send_test_alert():
    phone = "+916302305291"  # ✅ Your Twilio sandbox number with country code

    # ✅ Fetch jobs (this should return a list of dicts)
    jobs = fetch_jobs()
    if not jobs:
        return {"sent": False, "reason": "No jobs fetched"}

    job = jobs[0]  # Take the first job

    # ✅ Format message
    msg = (
        f"🚨 *New Job Alert!*\n\n"
        f"*Title:* {job.get('job_title')}\n"
        f"*Company:* {job.get('employer_name')}\n"
        f"*Type:* {job.get('job_employment_type')}\n"
        f"*Apply here:* {job.get('job_apply_link')}\n\n"
        f"Shared via Job Alert Bot 🤖"
    )

    # ✅ Send
    success = send_whatsapp(phone, msg)
    return {"sent": success, "message": msg}






router = APIRouter()

@router.post("/register")
def register_user(user: User):
    USERS_DB.append(user.dict())  # Save user to in-memory DB for now
    return {"message": f"✅ {user.name}, you have been registered successfully!"}

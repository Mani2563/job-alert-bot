# app/routes/recruiter.py

from fastapi import APIRouter, HTTPException
from app.services.job_matcher import match_users_with_job
from app.services.whatsapp_sender import send_whatsapp

router = APIRouter()

import os
import json

def load_users():
    if not os.path.exists("user_data.json"):
        # Create the file if it doesn't exist
        with open("user_data.json", "w") as f:
            json.dump([], f)
        return []

    with open("user_data.json", "r") as f:
        return json.load(f)

@router.post("/post_job")
async def post_job(job: dict):
    # 1. Log or save job (optional for now)
    
    # 2. Match job to relevant users
    matched_users = match_users_to_job(job, USERS_DB)

    # 3. Send WhatsApp to matched users
    for user in matched_users:
        send_whatsapp(user['phone'], f"New Job Alert 🚀:\n{job['title']} at {job['company']}\nApply here: {job['link']}")

    return {"message": f"Notified {len(matched_users)} users"}

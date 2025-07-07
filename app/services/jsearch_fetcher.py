import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def fetch_jobs(role="developer", location="India"):
    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    querystring = {
        "query": role,
        "location": location,
        "page": "1"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    try:
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print("❌ Error parsing JSON:", e)
        return []

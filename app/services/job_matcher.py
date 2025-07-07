import json

USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def match_users_with_job(job):
    matched_users = []
    users = load_users()

    for user in users:
        if user['domain'].lower() in job['title'].lower():
            if job.get('experience_required', 0) <= user['experience']:
                if user['preferred_location'].lower() in job['location'].lower():
                    matched_users.append(user)
    
    return matched_users

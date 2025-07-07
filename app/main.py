from fastapi import FastAPI
from app.routes import jobs, user

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Job Alert Bot is running!"}

app.include_router(jobs.router)
app.include_router(user.router)
from app.routes import register  # 👈 import your new route

app.include_router(register.router)  # 👈 register the route

from app.routes import user, recruiter

app = FastAPI()
app.include_router(user.router)
app.include_router(recruiter.router)



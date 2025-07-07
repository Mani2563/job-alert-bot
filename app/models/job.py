from pydantic import BaseModel
from typing import List

class Job(BaseModel):
    title: str
    company: str
    required_experience: int
    domains: List[str]
    mode: List[str]
    location: dict  # { country: str, city: str }
    link: str

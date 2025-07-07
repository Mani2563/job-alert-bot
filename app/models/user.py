from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    name: str
    phone: str = Field(..., pattern=r"^\+91\d{10}$")  # Use `pattern` instead of `regex`
    domains: List[str]
    mode: List[str]  # e.g. ['remote', 'hybrid']
    country: str
    city: str
    year_of_passout: int
    experience: int  # In years

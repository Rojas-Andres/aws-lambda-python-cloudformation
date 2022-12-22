from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    city: str = Field(..., min_length=3)
    email: str = Field(..., min_length=3)
    password: str = Field(..., min_length=3)


class UpdateUser(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    city: Optional[str]

class Login(BaseModel):
    email: str
    password: str
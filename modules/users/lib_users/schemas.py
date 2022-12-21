from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    nombre: str = Field(..., min_length=3)
    apellido: str = Field(..., min_length=3)
    ciudad: str = Field(..., min_length=3)


class UpdateUser(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    ciudad: Optional[str]
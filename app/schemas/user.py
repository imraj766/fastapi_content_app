from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email:EmailStr
    password:str


class UserIn(UserBase):
    pass

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at: datetime


class UserLogIn(BaseModel):
    email: EmailStr
    password: str

class TokenBase(BaseModel):
    id: Optional[int] = None
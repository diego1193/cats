from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class UserCreateRequest(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)


class UserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str
    email: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserLoginRequest(BaseModel):
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)


class UserLoginResponse(BaseModel):
    user: UserResponse
    message: str = "Login successful" 
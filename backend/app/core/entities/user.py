from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
        json_encoders = {datetime: lambda v: v.isoformat()}
        
    @classmethod
    def generate_username(cls, first_name: str, last_name: str, existing_usernames: set) -> str:
        base_username = f"{first_name.lower()}.{last_name.lower()}"
        username = base_username
        counter = 1
        
        while username in existing_usernames:
            username = f"{base_username}{counter}"
            counter += 1
            
        return username 
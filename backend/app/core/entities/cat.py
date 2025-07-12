from typing import Optional, Dict, Any
from pydantic import BaseModel


class CatBreed(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    origin: Optional[str] = None
    temperament: Optional[str] = None
    life_span: Optional[str] = None
    weight: Optional[Dict[str, str]] = None
    image: Optional[Dict[str, Any]] = None
    
    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> "CatBreed":
        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            description=data.get("description"),
            origin=data.get("origin"),
            temperament=data.get("temperament"),
            life_span=data.get("life_span"),
            weight=data.get("weight"),
            image=data.get("image")
        ) 
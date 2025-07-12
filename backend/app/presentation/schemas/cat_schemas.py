from pydantic import BaseModel
from typing import Optional, Dict, Any, List


class CatBreedResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    origin: Optional[str] = None
    temperament: Optional[str] = None
    life_span: Optional[str] = None
    weight: Optional[Dict[str, str]] = None
    image: Optional[Dict[str, Any]] = None
    
    class Config:
        from_attributes = True


class CatBreedListResponse(BaseModel):
    breeds: List[CatBreedResponse]
    count: int
    
    @classmethod
    def from_breeds(cls, breeds: List[CatBreedResponse]) -> "CatBreedListResponse":
        return cls(breeds=breeds, count=len(breeds)) 
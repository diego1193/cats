from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from app.core.entities.cat import CatBreed


class CatRepositoryInterface(ABC):
    
    @abstractmethod
    async def get_all_breeds(self) -> List[CatBreed]:
        pass
    
    @abstractmethod
    async def get_breed_by_id(self, breed_id: str) -> Optional[CatBreed]:
        pass
    
    @abstractmethod
    async def search_breeds(self, query_params: Dict[str, Any]) -> List[CatBreed]:
        pass 
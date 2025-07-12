from typing import Optional, List, Dict, Any
from app.core.entities.cat import CatBreed
from app.core.repositories.cat_repository import CatRepositoryInterface


class CatService:
    
    def __init__(self, cat_repository: CatRepositoryInterface):
        self.cat_repository = cat_repository
    
    async def get_all_breeds(self) -> List[CatBreed]:
        breeds = await self.cat_repository.get_all_breeds()
        return breeds
    
    async def get_breed_by_id(self, breed_id: str) -> Optional[CatBreed]:
        if not breed_id:
            raise ValueError("Breed ID cannot be empty")
        
        breed = await self.cat_repository.get_breed_by_id(breed_id)
        if not breed:
            raise ValueError(f"Breed with ID {breed_id} not found")
        
        return breed
    
    async def search_breeds(self, query_params: Dict[str, Any]) -> List[CatBreed]:
        if not query_params:
            return await self.get_all_breeds()
        
        breeds = await self.cat_repository.search_breeds(query_params)
        return breeds 
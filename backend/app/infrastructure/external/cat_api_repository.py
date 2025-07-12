import os
import httpx
from typing import Optional, List, Dict, Any
from app.core.entities.cat import CatBreed
from app.core.repositories.cat_repository import CatRepositoryInterface


class CatApiRepository(CatRepositoryInterface):
    
    def __init__(self):
        self.base_url = "https://api.thecatapi.com/v1"
        self.api_key = os.getenv("CAT_API_KEY", "live_JBT0Ah0Nt12iyl2IpjQVLDWjcLk0GQwf4zI9wBMfmfejKmcC31mOJp4yJz5TsOUP")
        self.headers = {"x-api-key": self.api_key}
    
    async def get_all_breeds(self) -> List[CatBreed]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/breeds", headers=self.headers)
            response.raise_for_status()
            
            breeds_data = response.json()
            return [CatBreed.from_api_response(breed) for breed in breeds_data]
    
    async def get_breed_by_id(self, breed_id: str) -> Optional[CatBreed]:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.base_url}/breeds/{breed_id}", headers=self.headers)
                response.raise_for_status()
                
                breed_data = response.json()
                return CatBreed.from_api_response(breed_data)
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    return None
                raise
    
    async def search_breeds(self, query_params: Dict[str, Any]) -> List[CatBreed]:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/breeds/search",
                params=query_params,
                headers=self.headers
            )
            response.raise_for_status()
            
            breeds_data = response.json()
            return [CatBreed.from_api_response(breed) for breed in breeds_data] 
import pytest
from unittest.mock import AsyncMock
from app.core.services.cat_service import CatService
from app.core.entities.cat import CatBreed
from app.core.repositories.cat_repository import CatRepositoryInterface


class MockCatRepository(CatRepositoryInterface):
    def __init__(self):
        self.breeds = [
            CatBreed(id="1", name="Siamese", description="A wonderful breed"),
            CatBreed(id="2", name="Persian", description="A fluffy breed"),
            CatBreed(id="3", name="Maine Coon", description="A large breed")
        ]
    
    async def get_all_breeds(self):
        return self.breeds
    
    async def get_breed_by_id(self, breed_id: str):
        return next((breed for breed in self.breeds if breed.id == breed_id), None)
    
    async def search_breeds(self, query_params):
        if "q" in query_params:
            query = query_params["q"].lower()
            return [breed for breed in self.breeds if query in breed.name.lower()]
        return self.breeds


@pytest.fixture
def mock_repository():
    return MockCatRepository()


@pytest.fixture
def cat_service(mock_repository):
    return CatService(mock_repository)


@pytest.mark.asyncio
async def test_get_all_breeds(cat_service):
    breeds = await cat_service.get_all_breeds()
    
    assert len(breeds) == 3
    assert breeds[0].name == "Siamese"
    assert breeds[1].name == "Persian"
    assert breeds[2].name == "Maine Coon"


@pytest.mark.asyncio
async def test_get_breed_by_id_success(cat_service):
    breed = await cat_service.get_breed_by_id("1")
    
    assert breed is not None
    assert breed.name == "Siamese"
    assert breed.description == "A wonderful breed"


@pytest.mark.asyncio
async def test_get_breed_by_id_not_found(cat_service):
    with pytest.raises(ValueError, match="Breed with ID 999 not found"):
        await cat_service.get_breed_by_id("999")


@pytest.mark.asyncio
async def test_get_breed_by_id_empty_id(cat_service):
    with pytest.raises(ValueError, match="Breed ID cannot be empty"):
        await cat_service.get_breed_by_id("")


@pytest.mark.asyncio
async def test_search_breeds_with_query(cat_service):
    breeds = await cat_service.search_breeds({"q": "siamese"})
    
    assert len(breeds) == 1
    assert breeds[0].name == "Siamese"


@pytest.mark.asyncio
async def test_search_breeds_no_results(cat_service):
    breeds = await cat_service.search_breeds({"q": "nonexistent"})
    
    assert len(breeds) == 0


@pytest.mark.asyncio
async def test_search_breeds_empty_params(cat_service):
    breeds = await cat_service.search_breeds({})
    
    assert len(breeds) == 3 
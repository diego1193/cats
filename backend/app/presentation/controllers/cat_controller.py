from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from app.core.services.cat_service import CatService
from app.infrastructure.external.cat_api_repository import CatApiRepository
from app.presentation.schemas.cat_schemas import CatBreedResponse, CatBreedListResponse


router = APIRouter(prefix="/breeds", tags=["Cat Breeds"])


def get_cat_service():
    cat_repository = CatApiRepository()
    return CatService(cat_repository)


@router.get("/", response_model=CatBreedListResponse)
async def get_all_breeds(cat_service: CatService = Depends(get_cat_service)):
    try:
        breeds = await cat_service.get_all_breeds()
        breed_responses = [CatBreedResponse(
            id=breed.id,
            name=breed.name,
            description=breed.description,
            origin=breed.origin,
            temperament=breed.temperament,
            life_span=breed.life_span,
            weight=breed.weight,
            image=breed.image
        ) for breed in breeds]
        
        return CatBreedListResponse.from_breeds(breed_responses)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search", response_model=CatBreedListResponse)
async def search_breeds(
    q: Optional[str] = Query(None, description="Search query"),
    limit: Optional[int] = Query(None, description="Limit results"),
    cat_service: CatService = Depends(get_cat_service)
):
    try:
        query_params = {}
        if q:
            query_params["q"] = q
        if limit:
            query_params["limit"] = limit
        
        breeds = await cat_service.search_breeds(query_params)
        breed_responses = [CatBreedResponse(
            id=breed.id,
            name=breed.name,
            description=breed.description,
            origin=breed.origin,
            temperament=breed.temperament,
            life_span=breed.life_span,
            weight=breed.weight,
            image=breed.image
        ) for breed in breeds]
        
        return CatBreedListResponse.from_breeds(breed_responses)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{breed_id}", response_model=CatBreedResponse)
async def get_breed_by_id(
    breed_id: str,
    cat_service: CatService = Depends(get_cat_service)
):
    try:
        breed = await cat_service.get_breed_by_id(breed_id)
        return CatBreedResponse(
            id=breed.id,
            name=breed.name,
            description=breed.description,
            origin=breed.origin,
            temperament=breed.temperament,
            life_span=breed.life_span,
            weight=breed.weight,
            image=breed.image
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.core.services.user_service import UserService
from app.infrastructure.database.mongo_user_repository import MongoUserRepository
from app.presentation.schemas.user_schemas import (
    UserCreateRequest, 
    UserResponse, 
    UserLoginRequest, 
    UserLoginResponse
)


router = APIRouter(prefix="/user", tags=["Users"])


def get_user_service():
    user_repository = MongoUserRepository()
    return UserService(user_repository)


@router.get("/", response_model=List[UserResponse])
async def get_users(user_service: UserService = Depends(get_user_service)):
    try:
        users = await user_service.get_all_users()
        return [UserResponse(
            id=str(user.id),
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        ) for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=UserResponse)
async def create_user(
    user_data: UserCreateRequest,
    user_service: UserService = Depends(get_user_service)
):
    try:
        user = await user_service.create_user(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password
        )
        return UserResponse(
            id=str(user.id),
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/login", response_model=UserLoginResponse)
async def login_user(
    username: str,
    password: str,
    user_service: UserService = Depends(get_user_service)
):
    try:
        user = await user_service.authenticate_user(username, password)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return UserLoginResponse(
            user=UserResponse(
                id=str(user.id),
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                email=user.email,
                created_at=user.created_at,
                updated_at=user.updated_at
            )
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
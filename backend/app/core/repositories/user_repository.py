from abc import ABC, abstractmethod
from typing import Optional, List
from app.core.entities.user import User


class UserRepositoryInterface(ABC):
    
    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass
    
    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        pass
    
    @abstractmethod
    async def get_user_by_username(self, username: str) -> Optional[User]:
        pass
    
    @abstractmethod
    async def get_user_by_email(self, email: str) -> Optional[User]:
        pass
    
    @abstractmethod
    async def get_all_users(self) -> List[User]:
        pass
    
    @abstractmethod
    async def get_existing_usernames(self) -> set:
        pass
    
    @abstractmethod
    async def update_user(self, user_id: str, user: User) -> Optional[User]:
        pass
    
    @abstractmethod
    async def delete_user(self, user_id: str) -> bool:
        pass 
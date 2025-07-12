from typing import Optional, List
from passlib.context import CryptContext
from app.core.entities.user import User
from app.core.repositories.user_repository import UserRepositoryInterface


class UserService:
    
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    async def create_user(self, first_name: str, last_name: str, email: str, password: str) -> User:
        existing_usernames = await self.user_repository.get_existing_usernames()
        username = User.generate_username(first_name, last_name, existing_usernames)
        
        existing_user = await self.user_repository.get_user_by_email(email)
        if existing_user:
            raise ValueError("Email already registered")
        
        hashed_password = self.pwd_context.hash(password)
        
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=hashed_password
        )
        
        return await self.user_repository.create_user(user)
    
    async def get_all_users(self) -> List[User]:
        return await self.user_repository.get_all_users()
    
    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        user = await self.user_repository.get_user_by_username(username)
        if not user:
            return None
        
        if not self.pwd_context.verify(password, user.password):
            return None
        
        return user
    
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await self.user_repository.get_user_by_id(user_id) 
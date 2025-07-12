from typing import Optional, List
from bson import ObjectId
from app.core.entities.user import User
from app.core.repositories.user_repository import UserRepositoryInterface
from app.infrastructure.database.config import db_config


class MongoUserRepository(UserRepositoryInterface):
    
    def __init__(self):
        self.collection_name = "users"
    
    @property
    def collection(self):
        return db_config.get_database()[self.collection_name]
    
    async def create_user(self, user: User) -> User:
        user_dict = user.dict(exclude={"id"})
        result = await self.collection.insert_one(user_dict)
        
        created_user = await self.collection.find_one({"_id": result.inserted_id})
        created_user["_id"] = str(created_user["_id"])  # Convert ObjectId to string
        return User(**created_user)
    
    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        try:
            user_data = await self.collection.find_one({"_id": ObjectId(user_id)})
            if user_data:
                user_data["_id"] = str(user_data["_id"])  # Convert ObjectId to string
                return User(**user_data)
        except Exception:
            return None
        return None
    
    async def get_user_by_username(self, username: str) -> Optional[User]:
        user_data = await self.collection.find_one({"username": username})
        if user_data:
            user_data["_id"] = str(user_data["_id"])  # Convert ObjectId to string
            return User(**user_data)
        return None
    
    async def get_user_by_email(self, email: str) -> Optional[User]:
        user_data = await self.collection.find_one({"email": email})
        if user_data:
            user_data["_id"] = str(user_data["_id"])  # Convert ObjectId to string
            return User(**user_data)
        return None
    
    async def get_all_users(self) -> List[User]:
        users = []
        async for user_data in self.collection.find():
            user_data["_id"] = str(user_data["_id"])  # Convert ObjectId to string
            users.append(User(**user_data))
        return users
    
    async def get_existing_usernames(self) -> set:
        usernames = set()
        async for user_data in self.collection.find({}, {"username": 1}):
            usernames.add(user_data["username"])
        return usernames
    
    async def update_user(self, user_id: str, user: User) -> Optional[User]:
        try:
            user_dict = user.dict(exclude={"id"})
            result = await self.collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": user_dict}
            )
            
            if result.modified_count > 0:
                updated_user = await self.collection.find_one({"_id": ObjectId(user_id)})
                updated_user["_id"] = str(updated_user["_id"])  # Convert ObjectId to string
                return User(**updated_user)
        except Exception:
            return None
        return None
    
    async def delete_user(self, user_id: str) -> bool:
        try:
            result = await self.collection.delete_one({"_id": ObjectId(user_id)})
            return result.deleted_count > 0
        except Exception:
            return False 
import os
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional


class DatabaseConfig:
    
    def __init__(self):
        self.mongodb_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
        self.database_name = os.getenv("DATABASE_NAME", "catapp")
        self.client: Optional[AsyncIOMotorClient] = None
        self.database = None
    
    async def connect(self):
        self.client = AsyncIOMotorClient(self.mongodb_url)
        self.database = self.client[self.database_name]
        
        try:
            await self.client.admin.command('ping')
            print("Connected to MongoDB successfully!")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise
    
    async def disconnect(self):
        if self.client:
            self.client.close()
            print("Disconnected from MongoDB")
    
    def get_database(self):
        return self.database


db_config = DatabaseConfig() 
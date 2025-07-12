import pytest
from unittest.mock import AsyncMock, Mock
from app.core.services.user_service import UserService
from app.core.entities.user import User
from app.core.repositories.user_repository import UserRepositoryInterface


class MockUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = []
        self.usernames = set()
    
    async def create_user(self, user: User) -> User:
        user.id = "test_id"
        self.users.append(user)
        self.usernames.add(user.username)
        return user
    
    async def get_user_by_id(self, user_id: str):
        return next((user for user in self.users if user.id == user_id), None)
    
    async def get_user_by_username(self, username: str):
        return next((user for user in self.users if user.username == username), None)
    
    async def get_user_by_email(self, email: str):
        return next((user for user in self.users if user.email == email), None)
    
    async def get_all_users(self):
        return self.users
    
    async def get_existing_usernames(self):
        return self.usernames
    
    async def update_user(self, user_id: str, user: User):
        pass
    
    async def delete_user(self, user_id: str):
        pass


@pytest.fixture
def mock_repository():
    return MockUserRepository()


@pytest.fixture
def user_service(mock_repository):
    return UserService(mock_repository)


@pytest.mark.asyncio
async def test_create_user_success(user_service):
    user = await user_service.create_user(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="password123"
    )
    
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john@example.com"
    assert user.username == "john.doe"
    assert user.id == "test_id"


@pytest.mark.asyncio
async def test_create_user_duplicate_email(user_service):
    await user_service.create_user(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="password123"
    )
    
    with pytest.raises(ValueError, match="Email already registered"):
        await user_service.create_user(
            first_name="Jane",
            last_name="Smith",
            email="john@example.com",
            password="password456"
        )


@pytest.mark.asyncio
async def test_authenticate_user_success(user_service):
    created_user = await user_service.create_user(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="password123"
    )
    
    authenticated_user = await user_service.authenticate_user("john.doe", "password123")
    
    assert authenticated_user is not None
    assert authenticated_user.username == "john.doe"


@pytest.mark.asyncio
async def test_authenticate_user_invalid_credentials(user_service):
    await user_service.create_user(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="password123"
    )
    
    authenticated_user = await user_service.authenticate_user("john.doe", "wrongpassword")
    
    assert authenticated_user is None


@pytest.mark.asyncio
async def test_get_all_users(user_service):
    await user_service.create_user("John", "Doe", "john@example.com", "password123")
    await user_service.create_user("Jane", "Smith", "jane@example.com", "password456")
    
    users = await user_service.get_all_users()
    
    assert len(users) == 2
    assert users[0].first_name == "John"
    assert users[1].first_name == "Jane" 
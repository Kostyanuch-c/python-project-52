import pytest

from task_manager.users.entities import UserChangeOrCreate
from task_manager.users.services.user_service import UserService


@pytest.fixture
def user_service() -> UserService:
    return UserService()


@pytest.fixture()
def user_create_data() -> UserChangeOrCreate:
    return UserChangeOrCreate(
        first_name="New first_name",
        last_name="New last_name",
        username="new_username",
        password="new12345612dsds",
    )

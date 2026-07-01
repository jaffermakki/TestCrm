from fastapi import HTTPException
from starlette import status

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository):

        self.repository = repository

    def register(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ):

        existing = self.repository.get_by_email(email)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=hash_password(password),
        )

        return self.repository.create(user)

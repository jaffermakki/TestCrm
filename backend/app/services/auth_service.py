from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from app.core.jwt import JWTManager
from app.core.password import verify_password
from app.repositories.user_repository import UserRepository


class AuthenticationService:

    def __init__(
        self,
        repository: UserRepository,
    ):

        self.repository = repository

    async def login(
        self,
        email: str,
        password: str,
    ):

        user = await self.repository.get_by_email(
            email
        )

        if user is None:

            raise HTTPException(
                HTTP_401_UNAUTHORIZED,
                "Invalid credentials",
            )

        if not verify_password(
            password,
            user.password_hash,
        ):

            raise HTTPException(
                HTTP_401_UNAUTHORIZED,
                "Invalid credentials",
            )

        return {

            "access_token":
                JWTManager.create_access_token(
                    str(user.id)
                ),

            "refresh_token":
                JWTManager.create_refresh_token(
                    str(user.id)
                )
        }

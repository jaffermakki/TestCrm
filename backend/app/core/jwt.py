from datetime import datetime
from datetime import timedelta
from datetime import timezone

from jose import jwt

from app.core.config import settings


class JWTManager:

    @staticmethod
    def create_access_token(
        subject: str,
    ) -> str:

        expire = datetime.now(
            timezone.utc
        ) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        payload = {
            "sub": subject,
            "type": "access",
            "exp": expire,
        }

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )

    @staticmethod
    def create_refresh_token(
        subject: str,
    ) -> str:

        expire = datetime.now(
            timezone.utc
        ) + timedelta(days=30)

        payload = {
            "sub": subject,
            "type": "refresh",
            "exp": expire,
        }

        return jwt.encode(
            payload,
            settings.SECRET_KEY,
            algorithm=settings.ALGORITHM,
        )

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.api.dependencies import get_database
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.schemas.user import UserRead
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserRead,
)
def register(

    request: UserCreate,

    db: Session = Depends(get_database),

):

    service = UserService(
        UserRepository(db),
    )

    return service.register(
        request.first_name,
        request.last_name,
        request.email,
        request.password,
    )

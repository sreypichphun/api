from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user
from models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user_endpoint(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, payload.email, payload.name)

@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


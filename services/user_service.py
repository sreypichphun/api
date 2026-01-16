from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.user import User

def create_user(db: Session, email: str, name: str):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

    user = User(email=email, name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

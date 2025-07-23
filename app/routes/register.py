from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate
from app.models.user_model import RegUser
from app.database.connection import SessionLocal

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
async def register_user(
    first_name: str = Form(...),
    age: int = Form(...),
    permanent_string_code: str = Form(...),
    state: str = Form(...),
    country: str = Form(...),
    db: Session = Depends(get_db)
):
    user = RegUser(
        first_name=first_name,
        age=age,
        permanent_string_code=permanent_string_code,
        state=state,
        country=country
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully"}

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.engine import db_session
from app.schema.user import UserCreate, UserRead
from app.services.user_service import create_user, get_user, get_users

users_router = APIRouter(prefix="/users", tags=["Users"])

# Endpoint to get all users
@users_router.get("/", response_model=list[UserRead]) # pasang response_model to specify the output schema, agar tidak null aja
def get_users_api(db: Session = Depends(db_session)):
  return get_users(db)

# Endpoint to get a specific user by ID
@users_router.get("/{user_id}", response_model=UserRead)
def get_user_api(user_id: str, db: Session = Depends(db_session)):
  return get_user(db, user_id)

# Endpoint to create a new user
@users_router.post("/", response_model=UserRead)
def create_user_api(user: UserCreate, db: Session = Depends(db_session)):
  new_user = create_user(db, user)
  return new_user

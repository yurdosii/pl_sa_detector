from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import crud, models, schemas
from src.db.database import SessionLocal

router = APIRouter(prefix="/users", tags=["user"])


# Dependency
def get_db():  # type: ignore [no-untyped-def]
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)) -> list[models.User]:
    return crud.get_users(db)


@router.post("/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
) -> schemas.User:
    return crud.create_user(db, user)

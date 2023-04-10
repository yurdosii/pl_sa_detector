from sqlalchemy.orm import Session

from . import models, schemas


def get_users(db: Session) -> list[models.User]:
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        username=user.username, age=user.age, first_name=user.first_name
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    age: int
    first_name: str | None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

    class Config:
        orm_mode = True

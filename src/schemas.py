import pydantic as _pd
import datetime as _dt
from typing import List


class _PostBase(_pd.BaseModel):
    title: str
    content: str


class _PostCreate(_PostBase):
    pass


class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class config:
        orm_mode = True


class _UserBase(_pd.BaseModel):
    email: str


class _UserCreate(_UserBase):
    password: str


class User(_UserBase):
    id: int
    is_active: bool
    posts: List[Post]

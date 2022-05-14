import pydantic as _pd
import datetime as _dt


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

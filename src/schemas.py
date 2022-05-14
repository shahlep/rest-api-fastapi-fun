import pydantic as _pd


class _PostBase(_pd.BaseModel):
    title: str
    content: str


class _PostCreate(_PostBase):
    pass

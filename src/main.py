import fastapi as _fastapi
from typing import List
import sqlalchemy.orm as _orm
import src.services as _services
import src.schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()


# https://fastapi.tiangolo.com/tutorial/sql-databases/
@app.post('/users/', response_model=_schemas.User)
def create_user(user: _schemas._UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db())):
    db_user = _services.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail='email already in use!')
    return _services.create_user(db=db, user=user)


@app.get('/users/', response_model=[_schemas.User])
def get_user(limit: int = 10, db: _orm.Session = _fastapi.Depends(_services.get_db())):
    pass

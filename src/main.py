import fastapi as _fastapi
import sqlalchemy.orm as _orm
import src.services as _services
import src.schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()


# https://fastapi.tiangolo.com/tutorial/sql-databases/
@app.post('/users/', response_model=_schemas.User)
def create_user(user: _schemas._UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db())):
    pass

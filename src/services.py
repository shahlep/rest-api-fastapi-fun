import src.database as _database
import sqlalchemy.orm as _orm
import src.models as _models, src.schemas as _schemas


# https://docs.sqlalchemy.org/en/14/core/metadata.html - how to create db using sqlalchemy
def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.Sessionlocal()
    try:
        yield db
    finally:
        db.close()


def get_user_by_email(db: _orm.Session, email: str):
    return db.query(_models.User).filter(_models.User.email == email).first()


def create_user(db: _orm.Session, user: _schemas._UserCreate):
    set_password = user.password  # not secure as no hashing done
    db_user = _models.User(email=user.email, password=set_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

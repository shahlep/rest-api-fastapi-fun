import database as _database


# https://docs.sqlalchemy.org/en/14/core/metadata.html - how to create db using sqlalchemy
def create_database():
    return _database.Base.metaData.create_all(bind=_database.engine)

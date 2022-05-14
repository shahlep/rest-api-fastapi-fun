import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database


class User(_database.Base):
    __tablename__ = 'users'
    id = _sql.column(_sql.Integer, primary_key=True, index=True)
    email = _sql.column(_sql.String, unique=True,index=True)
    password = _sql.column(_sql.String)
    is_active = _sql.column(_sql.Boolean, default=True)



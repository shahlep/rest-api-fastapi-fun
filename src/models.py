import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import datetime as _dt

import database as _database


class User(_database.Base):
    __tablename__ = 'users'
    id = _sql.column(_sql.Integer, primary_key=True, index=True)
    email = _sql.column(_sql.String, unique=True, index=True)
    password = _sql.column(_sql.String)
    is_active = _sql.column(_sql.Boolean, default=True)

    posts = _orm.relationship('Post', back_populates='owner')


class Post(_database.Base):
    __tablename__ = 'posts'
    id = _sql.column(_sql.Integer, primary_key=True, index=True)
    title = _sql.column(_sql.String, index=True)
    content = _sql.column(_sql.String, index=True)
    owner_id = _sql.column(_sql.Integer, _sql.ForeignKey('user.id'))

    date_created = _sql.column(_sql.DateTime, default=_dt.datetime.utcnow)
    date_last_updated = _sql.column(_sql.DateTime, default=_dt.datetime.utcnow)

    owner = _orm.relationship('User', back_populates='posts')

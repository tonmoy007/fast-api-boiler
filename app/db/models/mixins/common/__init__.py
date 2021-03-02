from datetime import datetime

from sqlalchemy import Integer, DateTime, Column
from sqlalchemy.ext.declarative import declared_attr

from app.db import db_session
from .soft_delete import SoftDeleteMixin


class DefaultMixin(object):
    """
    Set default tablename
    """

    @declared_attr
    def __tablename__(self, cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now,
                        index=True)
    query = db_session.query_property()
    base_query = db_session.query


class TimeStampMixin(object):
    created_at = Column(DateTime, nullable=False, default=datetime.now,
                        index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)

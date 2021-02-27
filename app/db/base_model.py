from sqlalchemy.exc import DatabaseError
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from app.db import db_session


class CustomBase(object):
    """This overrides the default
    `_declarative_constructor` constructor.
    It skips the attributes that are not present
    for the model, thus if a dict is passed with some
    unknown attributes for the model on creation,
    it won't complain for `unkwnown field`s.
    """

    def __init__(self, **kwargs):
        cls_ = type(self)
        for k in kwargs:
            if hasattr(cls_, k):
                setattr(self, k, kwargs[k])
            else:
                continue

    """
    Set default tablename
    """

    @declared_attr
    def __tablename__(self, cls):
        return cls.__name__.lower()

    """
    Add and try to flush.
    """

    def save(self):
        db_session.add(self)
        self._flush()
        return self

    """
    Update and try to flush.
    """

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        return self.save()

    """
    Delete and try to flush.
    """

    def delete(self):
        db_session.delete(self)
        self._flush()

    """
    Try to flush. If an error is raised,
    the session is rollbacked.
    """

    def _flush(self):
        try:
            db_session.flush()
        except DatabaseError as e:
            db_session.rollback()


BaseModel = declarative_base(cls=CustomBase, constructor=None)
BaseModel.query = db_session.query_property()
BaseModel.base_query = db_session.query
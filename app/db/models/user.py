from datetime import datetime

from graphql.pyutils.enum import __repr__
from sqlalchemy import Integer, Column, String, TIMESTAMP
from sqlalchemy.orm import relationship, backref

from app.db.base_model import BaseModel
from app.db.models.mixins import ModelSerializerMixin
from app.db.models.mixins.common import DefaultMixin
from app.db.models.mixins.common.soft_delete import SoftDeleteMixin


class User(BaseModel, ModelSerializerMixin, DefaultMixin, SoftDeleteMixin):
    __tablename__ = "users"
    ref_id = Column(Integer, index=True, nullable=False)
    ref_type = Column(String(255), nullable=False, default="partner", index=True)
    accounts = relationship("Account", cascade="all, delete",
                            passive_deletes=True)
    entries = relationship("Entry", cascade="all, delete", passive_deletes=True, backref=backref("entries"))
    updated_at = Column(TIMESTAMP, default=datetime.now, nullable=False)

    def __repr__(self):
        return f"Id:{self.id}, RefId:{self.ref_id}, CreatedAt:{self.created_at}"

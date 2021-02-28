from datetime import datetime

from sqlalchemy import Integer, Column, String, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.db.base_model import BaseModel
from app.db.serializers import ModelSerializerMixin


class User(BaseModel, ModelSerializerMixin):
    __tablename__ = "users"
    ref_id = Column(Integer, index=True, nullable=False)
    ref_type = Column(String(255), nullable=False, default="partner", index=True)
    accounts = relationship("Account", cascade="all, delete",
                            passive_deletes=True)
    entries = relationship("Entry", cascade="all, delete", passive_deletes=True)
    updated_at = Column(TIMESTAMP, default=datetime.now, nullable=False)

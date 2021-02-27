from sqlalchemy import Integer, Column, String, TIMESTAMP, text
from sqlalchemy.orm import relationship

from app.db.base_model import BaseModel
from app.db.serializers import ModelSerializerMixin


class User(BaseModel, ModelSerializerMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    ref_id = Column(Integer, index=True, nullable=False)
    ref_type = Column(String(255), nullable=False, default="partner", index=True)
    accounts = relationship("Account", back_ref="user", cascade="all, delete",
                            passive_deletes=True)
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), nullable=False)

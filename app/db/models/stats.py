from sqlalchemy import Column, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship

from app.db.base_model import BaseModel
from app.db.models.mixins import ModelSerializerMixin
from app.db.models.mixins.common import DefaultMixin, SoftDeleteMixin


class Stat(BaseModel, ModelSerializerMixin, DefaultMixin, SoftDeleteMixin):
    __tablename__ = "daily_account_stats"
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="cascade", onupdate="cascade"), index=True)
    account = relationship("Account")
    opening_balance = Column(Numeric(precision=2, scale=2))
    closing_balance = Column(Numeric(precision=2, scale=2))
    date = Column(Date, nullable=False, index=True)

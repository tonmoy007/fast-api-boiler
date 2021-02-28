import enum
from datetime import datetime

from sqlalchemy import Column, UnicodeText, JSON, Integer, ForeignKey, NUMERIC, TIMESTAMP, String
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import relationship, backref

from app.db.base_model import BaseModel
from app.db.serializers import ModelSerializerMixin


class EntrySource(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"
    DUE = "due"
    DEPOSIT = "deposit"
    POS = "pos"
    INVENTORY = "inventory"
    EMI = "emi"


class Entry(BaseModel, ModelSerializerMixin):
    __tablename__ = "entries"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade", onupdate="cascade"), nullable=False,
                     index=True)
    amount = Column(NUMERIC(precision=2, scale=2), default=0.00, nullable=False)
    user = relationship("User", backref=backref("entries", lazy="joined"))
    source_type = Column(ENUM(EntrySource), index=True, nullable=False)
    source_id = Column(Integer, nullable=True, index=True)
    customer_id = Column(Integer, nullable=True, index=True)
    emi_month = Column(Integer, nullable=True, index=True)
    note = Column(UnicodeText, nullable=True)
    attachments = Column(JSON, nullable=True)
    updated_at = Column(TIMESTAMP, default=datetime.now, nullable=False)
    created_from = Column(JSON, nullable=False)
    payment_id = Column(Integer, nullable=True)
    payment_method = Column(String(255), nullable=True)
    interest = Column(NUMERIC(precision=2, scale=2), default=0.00)
    bank_transaction_charge = Column(NUMERIC(precision=2, scale=2), default=0.00)

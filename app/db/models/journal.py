from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Numeric, UnicodeText, DATETIME, String, TIMESTAMP, text
from sqlalchemy.orm import relationship, backref

from app.db.base_model import BaseModel
from app.db.serializers import ModelSerializerMixin


class Journal(BaseModel, ModelSerializerMixin):
    __tablename__ = "journals"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="cascade", onupdate="cascade"), nullable=False,
                        index=True)
    sub_account_id = Column(Integer, ForeignKey("accounts.id", ondelete="cascade", onupdate="cascade"), nullable=False,
                            index=True)
    account = relationship("Account", cascade="all,delete,delete-orphan", backref=backref("journals", lazy="dynamic"))
    sub_account = relationship("Account", cascade="all,delete,delete-orphan",
                               backref=backref("journals", lazy="dynamic"))
    debit = Column(Numeric(precision=2, scale=2), default=0.00, nullable=False)
    credit = Column(Numeric(precision=2, scale=2), default=0.00, nullable=False)
    details = Column(UnicodeText, nullable=True)
    entry_at = Column(DATETIME, default=datetime.now, index=True)
    source_id = Column(Integer, nullable=False, index=True)
    source_type = Column(String(255), nullable=False, index=True)
    reference = Column(String(255), nullable=True)
    receiver_type = Column(String(255), nullable=True, index=True)
    receiver_id = Column(Integer, nullable=True, index=True)

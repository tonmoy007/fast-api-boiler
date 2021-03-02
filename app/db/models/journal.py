from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Numeric, UnicodeText, DATETIME, String
from sqlalchemy.orm import relationship

from app.db.base_model import BaseModel
from app.db.models.mixins import ModelSerializerMixin
from app.db.models.mixins.common import DefaultMixin, SoftDeleteMixin


class Journal(BaseModel, DefaultMixin, ModelSerializerMixin, SoftDeleteMixin):
    __tablename__ = "journals"
    account_id = Column(Integer, ForeignKey("accounts.id", ondelete="cascade", onupdate="cascade"), nullable=False,
                        index=True)
    sub_account_id = Column(Integer, ForeignKey("accounts.id", ondelete="cascade", onupdate="cascade"), nullable=False,
                            index=True)
    # account = relationship("Account", cascade="all,delete,delete-orphan", backref=backref("journals", lazy="dynamic"))
    sub_account = relationship("Account",
                               foreign_keys=sub_account_id)
    debit = Column(Numeric(precision=2, scale=2), default=0.00, nullable=False)
    credit = Column(Numeric(precision=2, scale=2), default=0.00, nullable=False)
    details = Column(UnicodeText, nullable=True)
    entry_at = Column(DATETIME, default=datetime.now, index=True)
    source_id = Column(Integer, nullable=False, index=True)
    source_type = Column(String(255), nullable=False, index=True)
    reference = Column(String(255), nullable=True)
    receiver_type = Column(String(255), nullable=True, index=True)
    receiver_id = Column(Integer, nullable=True, index=True)

from datetime import datetime

from sqlalchemy import Column, Integer, String, UnicodeText, ForeignKey, UniqueConstraint, TIMESTAMP, text, Boolean, \
    Unicode
from sqlalchemy.orm import relationship, backref

from app.db.base_model import BaseModel
from app.db.serializers import ModelSerializerMixin


class Account(BaseModel, ModelSerializerMixin):
    __tablename__ = "accounts"

    __table_args__ = (
        UniqueConstraint("user_id", "key"),
    )
    """
    Model Columns And Relations
    """
    name = Column(String(255), nullable=False)
    name_bn = Column(Unicode(255), nullable=False)
    details = Column(UnicodeText, nullable=True)
    key = Column(String(255), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", backref("accounts", lazy="dynamic"))
    parent_id = Column(Integer, ForeignKey("accounts.id", ondelete="CASCADE"), nullable=True)
    parent = relationship("Account", remote_side=[id], back_populates="children")
    children = relationship("Account", backref=backref('parent', remote_side=[id], lazy="joined", join_depth=4),
                            cascade="all,delete,delete-orphan", lazy="joined", join_depth=4)
    journals = relationship("Journal", cascade="all,delete,delete-orphan",
                            backref=backref("account", lazy="dynamic"))
    layer = Column(Integer, nullable=False, default=2)
    root_account = Column(String(255), nullable=False)
    account_type = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    visible = Column(Boolean, default=False)
    editable = Column(Boolean, default=False)
    deletable = Column(Boolean, default=False)
    updated_at = Column(TIMESTAMP, default=datetime.now())

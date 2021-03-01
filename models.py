from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.dialects import postgresql
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    logo = Column(String)
    description = Column(Text)
    slug = Column(String)
    featured = Column(Boolean, default=False)
    status = Column(Integer, index=True, default=0)
    order = Column(Integer, index=True, default=0)
    route_id = Column(Integer, default=0)
    metatags = Column(postgresql.JSON)
    created_at = Column(DateTime, index=True, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

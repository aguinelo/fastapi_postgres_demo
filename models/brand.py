from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime
from sqlalchemy.dialects import postgresql
from datetime import datetime

from database import Base


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

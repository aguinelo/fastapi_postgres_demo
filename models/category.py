from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from database import Base
from models.product import product_category_association_table


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    name = Column(String)
    description = Column(String)
    level = Column(Integer, default=1)
    order = Column(Integer, default=0, index=True)
    status = Column(Integer, default=1, index=True)
    route_id = Column(Integer)
    metatags = Column(postgresql.JSON)
    created_at = Column(DateTime, index=True, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    parent = relationship("Category")
    products = relationship('Product', secondary=product_category_association_table, back_populates='categories')

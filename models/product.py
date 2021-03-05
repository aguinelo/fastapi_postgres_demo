from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base

product_category_association_table = Table(
    'products_categoies',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    created_at = Column(DateTime, index=True, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    brand = relationship("Brand")
    categories = relationship('Category', secondary=product_category_association_table, back_populates='products')

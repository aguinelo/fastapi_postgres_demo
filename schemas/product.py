from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class ProductBrand(BaseModel):
    id: int
    name: str
    logo: str

    class Config:
        orm_mode = True


class ProductCategory(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    brand_id: int
    categories: List[Optional[int]] = []


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductResponse(Product):
    brand: ProductBrand
    categories: Optional[List[ProductCategory]] = []
    created_at: datetime

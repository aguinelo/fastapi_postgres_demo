from datetime import datetime

from pydantic import BaseModel


# response in product
class ProductBrand(BaseModel):
    id: int
    name: str
    logo: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    brand_id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductResponse(Product):
    brand: ProductBrand
    created_at: datetime

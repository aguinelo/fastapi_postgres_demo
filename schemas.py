from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Json
from datetime import datetime

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "aguinelo": {
        "username": "aguinelo",
        "full_name": "Koczkodai",
        "email": "aguinelo@gmail.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Customer(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class CustomerInDb(Customer):
    hashed_password: str


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class BrandBase(BaseModel):
    name: str
    logo: str
    description: str
    slug: str
    featured: Optional[bool] = False
    status: Optional[int] = 0
    metatags: Dict[str, Any]


class ItemCreate(ItemBase):
    pass


class BrandCreate(BrandBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class Brand(BaseModel):
    id: int
    name: str
    logo: str
    description: str
    slug: str
    featured: bool
    status: int
    metatags: Optional[Dict[str, Any]] = []

    class Config:
        orm_mode = True


# response in product
class ProductBrand(BaseModel):
    id: int
    name: str
    logo: str

    class Config:
        orm_mode = True


class BrandResponse(Brand):
    order: int
    created_at: datetime
    route_id: int

    pass


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

from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime


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

    class Config:
        orm_mode = True


class BrandResponse(Brand):
    order: int
    created_at: datetime
    route_id: int

    pass

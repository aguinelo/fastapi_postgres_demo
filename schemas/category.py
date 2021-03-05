from datetime import datetime
from typing import Optional, Any, Dict

from pydantic import BaseModel


class CategoryBase(BaseModel):
    parent_id: Optional[int] = None
    name: str
    description: str
    level: int
    order: int
    status: int
    route_id: int
    metatags: Optional[Dict[str, Any]] = {}


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: str

    class Config:
        orm_mode = True


class CategoryResponse(Category):
    created_at: datetime

    pass

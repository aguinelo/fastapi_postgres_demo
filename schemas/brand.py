from datetime import datetime
from typing import Optional, Any, Dict

from pydantic import BaseModel


class BrandBase(BaseModel):
    name: str
    logo: str
    description: str
    slug: str
    featured: Optional[bool] = False
    status: Optional[int] = 0
    metatags: Dict[str, Any]


class BrandCreate(BrandBase):
    pass


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


class BrandResponse(Brand):
    order: int
    created_at: datetime
    route_id: int

    pass

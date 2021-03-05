from pydantic import BaseModel


class ProductCategoryBase(BaseModel):
    product_id: int
    category_id: int


class ProductCategoryCreate(ProductCategoryBase):
    pass

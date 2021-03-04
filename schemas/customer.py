from typing import Optional

from pydantic import BaseModel


class Customer(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class CustomerInDb(Customer):
    hashed_password: str

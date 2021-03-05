from fastapi import HTTPException
from sqlalchemy import Integer
from sqlalchemy.orm import Session

from models.user import User as UserModel
from models.item import Item as ItemModel
from models.brand import Brand as BrandModel
from models.product import Product as ProductModel
from models.category import Category as CategoryModel
from schemas.category import CategoryCreate
from schemas.product_category import ProductCategoryCreate
from schemas.user import UserCreate
from schemas.item import ItemCreate
from schemas.brand import BrandCreate
from schemas.product import ProductCreate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = UserModel(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemModel).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = ItemModel(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_brand(db: Session, data: BrandCreate):
    brand = BrandModel(**data.dict())

    # faz as treta de route_id aqui, ou pode injetar qualquer lógica
    brand.route_id = 10

    db.add(brand)
    db.commit()
    db.refresh(brand)
    return brand


def create_product(db: Session, data: ProductCreate):
    categories = db.query(CategoryModel).filter(CategoryModel.id.in_(data.categories)).all()

    if len(categories) != len(data.categories):
        _not_found = list(map(str, filter(
            lambda category: category if category not in map(lambda c_: c_.id, categories) else None,
            data.categories
        )))

        raise HTTPException(status_code=404, detail=f"Categories: {','.join(_not_found)} not found.")
    data.categories = categories
    product = ProductModel(**data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BrandModel).offset(skip).limit(limit).all()


def get_brands_by_json(db: Session, skip: int = 0, limit: int = 100):
    # return db.query(models.Brand).filter(models.Brand.metatags["opa"].cast(int) == 123).offset(skip).limit(limit).all()
    return db.query(BrandModel).filter(
        BrandModel.metatags['opa'].astext.cast(Integer) == 321
    ).offset(skip).limit(limit).all()


# categories

def create_category(db: Session, data: CategoryCreate):
    category = CategoryModel(**data.dict())
    # TODO replace for route create
    category.route_id = 0
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

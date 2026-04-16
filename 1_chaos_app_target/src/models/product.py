from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Index

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.category import Category
    from src.models.order_item import OrderItem
    

class Product(SQLModel, table=True):
   
    product_id: str = Field(primary_key=True)

    product_category_id: int | None = Field(
        default=None, foreign_key="category.category_id"
    )
    
    product_name_length: int | None
    product_description_length: int | None
    product_photos_qty: int | None

    product_weight_g: int | None
    product_length_cm: int | None
    product_height_cm: int | None
    product_width_cm: int | None

    category: "Category" = Relationship(back_populates="products")
    order_items: list["OrderItem"] = Relationship(back_populates="product")

    # __table_args__ = (
    #     Index("idx_category_price", "category", "price"),
    # )

class ProductCreate(SQLModel):
    
    product_id: str | None
    product_category_id: int | None
    
    product_name_length: int | None
    product_description_length: int | None
    product_photos_qty: int | None

    product_weight_g: int | None
    product_length_cm: int | None
    product_height_cm: int | None
    product_width_cm: int | None
    

class ProductPublic(SQLModel):
    
    product_id: str | None
    product_category_id: int | None
    
    product_name_length: int | None
    product_description_length: int | None
    product_photos_qty: int | None

    product_weight_g: int | None
    product_length_cm: int | None
    product_height_cm: int | None
    product_width_cm: int | None
    
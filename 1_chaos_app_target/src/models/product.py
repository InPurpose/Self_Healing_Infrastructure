from sqlmodel import Field, SQLModel, Relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.category import Category
    

class Product(SQLModel, table=True):
   
    product_id: str | None = Field(primary_key=True)

    product_category_name: str | None = Field(
        default=None, foreign_key="category.name"
    )
    
    product_name_length: int | None
    product_description_length: int | None
    product_photos_qty: int | None

    product_weight_g: int | None
    product_length_cm: int | None
    product_height_cm: int | None
    product_width_cm: int | None

    category: "Category" = Relationship(back_populates="products")

class ProductCreate(SQLModel):
    
    product_id: str | None
    product_category_name: str | None 
    
    product_name_length: int | None
    product_description_length: int | None
    product_photos_qty: int | None

    product_weight_g: int | None
    product_length_cm: int | None
    product_height_cm: int | None
    product_width_cm: int | None
    

class ProductPublic(SQLModel):
    
    product_id: str | None
    product_category_name: str | None 
    
    product_name_length: int | None
    product_description_length: int | None
    product_photos_qty: int | None

    product_weight_g: int | None
    product_length_cm: int | None
    product_height_cm: int | None
    product_width_cm: int | None
    
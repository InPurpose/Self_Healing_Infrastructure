from sqlmodel import Field, SQLModel, Relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.product import Product

class Category(SQLModel, table=True):
    # category_id: str = Field(primary_key=True)
    category_id: int | None = Field(default=None, primary_key=True)
    name: str | None 
    name_english: str | None

    products: list["Product"] = Relationship(back_populates="category")

class CategoryCreate(SQLModel):
    name: str | None
    name_english: str | None

class CategoryPublic(SQLModel):
    name: str | None
    name_english: str | None
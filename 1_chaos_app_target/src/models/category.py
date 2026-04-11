from sqlmodel import Field, SQLModel, Relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.product import Product

class Category(SQLModel, table=True):
    name: str | None = Field(primary_key=True)
    name_english: str | None

    products: list["Product"] = Relationship(back_populates="category")

class CategoryCreate(SQLModel):
    name: str | None
    name_english: str | None

class CategoryPublic(SQLModel):
    name: str | None
    name_english: str | None
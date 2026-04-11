from sqlmodel import Field, SQLModel, Relationship

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from src.models.product import Product

class GeoLocation(SQLModel, table=True):

    zip_code: int | None = Field(primary_key=True)
    lantitude: float | None 
    longtitude: float  | None 
    city: str | None
    state: str | None 

class GeoLocationCreate(SQLModel):

    zip_code: int | None 
    city: str | None
    state: str | None 

class GeoLocationPublic(SQLModel):

    zip_code: int | None
    lantitude: float | None 
    longtitude: float  | None 
    city: str | None
    state: str | None 
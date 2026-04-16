from sqlmodel import Field, SQLModel, Relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.seller import Seller
    from src.models.customer import Customer

class GeoLocation(SQLModel, table=True):

    zipcode: str = Field(primary_key=True)
    latitude: float | None 
    longtitude: float  | None 
    city: str | None
    state: str | None 

    # sellers: "Seller" = Relationship(back_populates="locations")
    # customer: "Customer" = Relationship(back_populates="locations")
    sellers: list["Seller"] = Relationship(back_populates="location")
    customers: list["Customer"] = Relationship(back_populates="location")

class GeoLocationCreate(SQLModel):

    zipcode: str | None 
    city: str | None
    state: str | None 

class GeoLocationPublic(SQLModel):

    zipcode: str | None
    latitude: float | None 
    longtitude: float  | None 
    city: str | None
    state: str | None 
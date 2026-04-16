from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Index

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.geolocation import GeoLocation
    from src.models.order_item import OrderItem
    

class Seller(SQLModel, table=True):
   
    seller_id: str = Field(primary_key=True)

    seller_zipcode: str | None = Field(
        default=None, foreign_key="geolocation.zipcode"
    )

    seller_city: str | None
    seller_state: str | None
    

    location: "GeoLocation" = Relationship(back_populates="sellers")
    order_items: list["OrderItem"] = Relationship(back_populates="seller")


class SellerCreate(SQLModel):
    seller_id: str | None 
    seller_zipcode: str | None 
    seller_city: str | None
    seller_state: str | None
 
class SellerPublic(SQLModel):
    seller_id: str | None 
    seller_zipcode: str | None 
    seller_city: str | None
    seller_state: str | None
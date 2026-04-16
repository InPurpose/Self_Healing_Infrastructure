from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Index

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.geolocation import GeoLocation
    from src.models.order import Order
    

class Customer(SQLModel, table=True):
   
    customer_id: str = Field(primary_key=True)
    customer_unique_id: str | None 


    customer_zipcode: str | None = Field(
        default=None, foreign_key="geolocation.zipcode"
    )

    customer_city: str | None
    customer_state: str | None
    

    location: "GeoLocation" = Relationship(back_populates="customers")
    orders: "Order" = Relationship(back_populates="customer")

class CustomerCreate(SQLModel):
    customer_id: str | None
    customer_unique_id: str | None 

    customer_zipcode: str | None 
    customer_city: str | None
    customer_state: str | None
    

class CustomerPublic(SQLModel):
    customer_id: str | None
    customer_unique_id: str | None 

    customer_zipcode: str | None 
    customer_city: str | None
    customer_state: str | None
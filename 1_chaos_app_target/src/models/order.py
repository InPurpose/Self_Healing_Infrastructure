from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Index

from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.customer import Customer
    from src.models.order_item import OrderItem
    from src.models.order_review import OrderReview
    from src.models.order_payment import OrderPayment
    

class Order(SQLModel, table=True):
   
    order_id: str = Field(primary_key=True)

    customer_id: str = Field(
        foreign_key="customer.customer_id"
    )

    order_status: str | None
    
    order_purchase_timestamp: datetime | None
    order_approved_at: datetime | None
    order_delivered_carrier_date: datetime | None
    order_delivered_customer_date: datetime | None
    order_estimated_delivery_date: datetime | None


    customer: "Customer" = Relationship(back_populates="orders")
    order_items: list["OrderItem"] = Relationship(back_populates="order")
    order_reviews: list["OrderReview"] = Relationship(back_populates="order")
    order_payments: list["OrderPayment"] = Relationship(back_populates="order")

class OrderCreate(SQLModel):

    order_id: str | None 

    customer_id: str | None
    order_status: str | None
    
    order_purchase_timestamp: datetime | None
    order_approved_at: datetime | None
    order_delivered_carrier_date: datetime | None
    order_delivered_customer_date: datetime | None
    order_estimated_delivery_date: datetime | None
 
class OrderPublic(SQLModel):
    order_id: str | None 

    customer_id: str | None
    order_status: str | None
    
    order_purchase_timestamp: datetime | None
    order_approved_at: datetime | None
    order_delivered_carrier_date: datetime | None
    order_delivered_customer_date: datetime | None
    order_estimated_delivery_date: datetime | None

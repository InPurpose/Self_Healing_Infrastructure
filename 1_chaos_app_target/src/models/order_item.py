from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Index

from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.order import Order
    from src.models.product import Product
    from src.models.seller import Seller
    

class OrderItem(SQLModel, table=True):
   
    order_id: str | None = Field(
        foreign_key="order.order_id",
        primary_key=True
    )
    order_item_id: str = Field(primary_key=True)
    

    product_id : str | None = Field(
        foreign_key="product.product_id"
    )

    seller_id: str | None = Field(
        foreign_key="seller.seller_id"
    )
    
    shipping_limit_date: datetime | None
    price: float | None
    freight_value: float | None


    order: "Order" = Relationship(back_populates="order_items")
    product: "Product" = Relationship(back_populates="order_items")
    seller: "Seller" = Relationship(back_populates="order_items")

class OrderItemCreate(SQLModel):

    order_item_id: str | None

    order_id: str | None 
    product_id : str | None
    seller_id: str | None 
    
    shipping_limit_date: datetime | None
    price: float | None
    freight_value: float | None


class OrderItemPublic(SQLModel):
    order_item_id: str | None

    order_id: str | None 
    product_id : str | None
    seller_id: str | None 
    
    shipping_limit_date: datetime | None
    price: float | None
    freight_value: float | None



"order_id","order_item_id",
"product_id","seller_id",
"shipping_limit_date","price",
"freight_value"
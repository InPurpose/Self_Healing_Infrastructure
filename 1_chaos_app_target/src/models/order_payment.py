from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Index

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.order import Order
    

class OrderPayment(SQLModel, table=True):
   
    order_id: str = Field(
        primary_key=True, 
        foreign_key="order.order_id"
        )

    payment_sequential : int = Field(primary_key=True)

    payment_type: str | None
    payment_installment: int | None
    payment_value: float | None

    order: "Order" = Relationship(back_populates="order_payments")

class OrderPaymentCreate(SQLModel):

    order_id: str | None

    payment_sequential : int | None
    payment_type: str | None
    payment_installment: int | None
    payment_value: float | None


class OrderPaymentPublic(SQLModel):

    order_id: str | None

    payment_sequential : int | None
    payment_type: str | None
    payment_installment: int | None
    payment_value: float | None

from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Index

from datetime import datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.order import Order
    

class OrderReview(SQLModel, table=True):
   
    review_id: str = Field(primary_key=True)
    order_id: str = Field(
        foreign_key="order.order_id"
        )

    review_score : int | None

    review_comment_title: str | None
    review_comment_message: str | None

    review_creation_date: datetime | None
    review_answer_timestamp: datetime | None


    order: "Order" = Relationship(back_populates="order_reviews")

class OrderReviewCreate(SQLModel):

    review_id: str | None 
    order_id: str | None 

    review_score : int | None

    review_comment_title: str | None
    review_comment_message: str | None
    review_creation_date: datetime | None
    review_answer_timestamp: datetime | None


class OrderReviewPublic(SQLModel):

    review_id: str | None 
    order_id: str | None 

    review_score : int | None

    review_comment_title: str | None
    review_comment_message: str | None
    review_creation_date: datetime | None
    review_answer_timestamp: datetime | None

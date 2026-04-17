"""rename order table to orders table

Revision ID: 8bbe2849578a
Revises: 246d7153288b
Create Date: 2026-04-17 16:52:44.549151

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '8bbe2849578a'
down_revision: Union[str, Sequence[str], None] = '246d7153288b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_table("order", "orders")



def downgrade() -> None:
    """Downgrade schema."""
    op.rename_table("orders", "order")
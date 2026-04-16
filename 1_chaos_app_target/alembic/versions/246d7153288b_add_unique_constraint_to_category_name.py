"""add unique constraint to category name

Revision ID: 246d7153288b
Revises: 1d82d0d9ec4f
Create Date: 2026-04-16 16:03:57.739212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '246d7153288b'
down_revision: Union[str, Sequence[str], None] = '1d82d0d9ec4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(
        "unique_category_name",   # constraint 名字
        "category",               # 表名
        ["name"]                  # 列
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "unique_category_name",
        "category",
        type_="unique"
    )

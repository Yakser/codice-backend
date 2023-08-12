"""remove test field

Revision ID: f15119db1d2f
Revises: c5406e235440
Create Date: 2023-08-11 23:43:45.148586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "f15119db1d2f"
down_revision: Union[str, None] = "c5406e235440"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("paste", "new_field")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("paste", sa.Column("new_field", sa.INTEGER(), nullable=False))
    # ### end Alembic commands ###
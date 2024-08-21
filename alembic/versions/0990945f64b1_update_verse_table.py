"""update verse table

Revision ID: 0990945f64b1
Revises: d89c65ef679f
Create Date: 2024-08-18 16:04:14.945666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0990945f64b1'
down_revision: Union[str, None] = 'd89c65ef679f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('verses', sa.Column('title', sa.String(), nullable=True))
    op.add_column('verses', sa.Column('said_jesus', sa.Boolean(), nullable=True, default=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('verses', 'said_jesus')
    op.drop_column('verses', 'title')
    # ### end Alembic commands ###
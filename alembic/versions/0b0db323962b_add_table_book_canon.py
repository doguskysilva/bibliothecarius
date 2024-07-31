"""add table book_canon

Revision ID: 0b0db323962b
Revises: a1bb2cd33227
Create Date: 2024-07-31 01:16:41.590255

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0b0db323962b"
down_revision: Union[str, None] = "a1bb2cd33227"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "book_canon",
        sa.Column("book_canon_id", sa.Integer(), nullable=False),
        sa.Column("canon_id", sa.Integer(), nullable=False),
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.Column("sort_index", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["book_id"],
            ["books.book_id"],
        ),
        sa.ForeignKeyConstraint(
            ["canon_id"],
            ["canons.canon_id"],
        ),
        sa.PrimaryKeyConstraint("book_canon_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("book_canon")
    # ### end Alembic commands ###
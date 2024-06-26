"""Added books table

Revision ID: 15e4ddfdfbdd
Revises: 765539ab96d4
Create Date: 2024-06-07 16:05:57.678230

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "15e4ddfdfbdd"
down_revision: Union[str, None] = "765539ab96d4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "books",
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.Column("testament", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("abbreviation", sa.String(), nullable=False),
        sa.Column("total_chapters", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("book_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("books")
    # ### end Alembic commands ###

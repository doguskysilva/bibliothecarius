"""rename columns to room convention

Revision ID: 9f6f58f7f7fd
Revises: f2c4a4c8936a
Create Date: 2026-02-17 04:43:48.757000

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9f6f58f7f7fd"
down_revision: Union[str, None] = "f2c4a4c8936a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("books") as batch_op:
        batch_op.alter_column("book_id", new_column_name="id", existing_type=sa.Integer())
        batch_op.alter_column(
            "total_chapters", new_column_name="totalChapters", existing_type=sa.Integer()
        )

    with op.batch_alter_table("canons") as batch_op:
        batch_op.alter_column("canon_id", new_column_name="id", existing_type=sa.Integer())
        batch_op.alter_column(
            "total_books", new_column_name="totalBooks", existing_type=sa.Integer()
        )

    with op.batch_alter_table("translations") as batch_op:
        batch_op.alter_column(
            "translation_id", new_column_name="id", existing_type=sa.Integer()
        )
        batch_op.alter_column("canon_id", new_column_name="canonId", existing_type=sa.Integer())
        batch_op.alter_column(
            "total_verses", new_column_name="totalVerses", existing_type=sa.Integer()
        )

    with op.batch_alter_table("verses") as batch_op:
        batch_op.alter_column("verse_id", new_column_name="id", existing_type=sa.Integer())
        batch_op.alter_column(
            "translation_id", new_column_name="translationId", existing_type=sa.Integer()
        )
        batch_op.alter_column("book_id", new_column_name="bookId", existing_type=sa.Integer())
        batch_op.alter_column(
            "verse_number", new_column_name="verseNumber", existing_type=sa.Integer()
        )
        batch_op.alter_column(
            "said_jesus", new_column_name="saidJesus", existing_type=sa.Integer()
        )

    with op.batch_alter_table("book_canon") as batch_op:
        batch_op.alter_column(
            "book_canon_id", new_column_name="id", existing_type=sa.Integer()
        )
        batch_op.alter_column("canon_id", new_column_name="canonId", existing_type=sa.Integer())
        batch_op.alter_column("book_id", new_column_name="bookId", existing_type=sa.Integer())
        batch_op.alter_column(
            "sort_index", new_column_name="sortIndex", existing_type=sa.Integer()
        )

    with op.batch_alter_table("bookmarks") as batch_op:
        batch_op.alter_column(
            "bookmark_id", new_column_name="id", existing_type=sa.Integer()
        )
        batch_op.alter_column(
            "translation_id", new_column_name="translationId", existing_type=sa.Integer()
        )
        batch_op.alter_column("book_id", new_column_name="bookId", existing_type=sa.Integer())
        batch_op.alter_column(
            "created_at", new_column_name="createdAt", existing_type=sa.Integer()
        )
        batch_op.alter_column(
            "updated_at", new_column_name="updatedAt", existing_type=sa.Integer()
        )

    with op.batch_alter_table("favorites") as batch_op:
        batch_op.alter_column("favorite_id", new_column_name="id", existing_type=sa.Integer())
        batch_op.alter_column("verse_id", new_column_name="verseId", existing_type=sa.Integer())
        batch_op.alter_column(
            "created_at", new_column_name="createdAt", existing_type=sa.Integer()
        )
        batch_op.alter_column(
            "updated_at", new_column_name="updatedAt", existing_type=sa.Integer()
        )


def downgrade() -> None:
    with op.batch_alter_table("favorites") as batch_op:
        batch_op.alter_column("id", new_column_name="favorite_id", existing_type=sa.Integer())
        batch_op.alter_column("verseId", new_column_name="verse_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "createdAt", new_column_name="created_at", existing_type=sa.Integer()
        )
        batch_op.alter_column(
            "updatedAt", new_column_name="updated_at", existing_type=sa.Integer()
        )

    with op.batch_alter_table("bookmarks") as batch_op:
        batch_op.alter_column("id", new_column_name="bookmark_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "translationId", new_column_name="translation_id", existing_type=sa.Integer()
        )
        batch_op.alter_column("bookId", new_column_name="book_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "createdAt", new_column_name="created_at", existing_type=sa.Integer()
        )
        batch_op.alter_column(
            "updatedAt", new_column_name="updated_at", existing_type=sa.Integer()
        )

    with op.batch_alter_table("book_canon") as batch_op:
        batch_op.alter_column("id", new_column_name="book_canon_id", existing_type=sa.Integer())
        batch_op.alter_column("canonId", new_column_name="canon_id", existing_type=sa.Integer())
        batch_op.alter_column("bookId", new_column_name="book_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "sortIndex", new_column_name="sort_index", existing_type=sa.Integer()
        )

    with op.batch_alter_table("verses") as batch_op:
        batch_op.alter_column("id", new_column_name="verse_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "translationId", new_column_name="translation_id", existing_type=sa.Integer()
        )
        batch_op.alter_column("bookId", new_column_name="book_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "verseNumber", new_column_name="verse_number", existing_type=sa.Integer()
        )
        batch_op.alter_column(
            "saidJesus", new_column_name="said_jesus", existing_type=sa.Integer()
        )

    with op.batch_alter_table("translations") as batch_op:
        batch_op.alter_column("id", new_column_name="translation_id", existing_type=sa.Integer())
        batch_op.alter_column("canonId", new_column_name="canon_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "totalVerses", new_column_name="total_verses", existing_type=sa.Integer()
        )

    with op.batch_alter_table("canons") as batch_op:
        batch_op.alter_column("id", new_column_name="canon_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "totalBooks", new_column_name="total_books", existing_type=sa.Integer()
        )

    with op.batch_alter_table("books") as batch_op:
        batch_op.alter_column("id", new_column_name="book_id", existing_type=sa.Integer())
        batch_op.alter_column(
            "totalChapters", new_column_name="total_chapters", existing_type=sa.Integer()
        )

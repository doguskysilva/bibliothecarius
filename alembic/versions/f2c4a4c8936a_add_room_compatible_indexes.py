"""add room compatible indexes

Revision ID: f2c4a4c8936a
Revises: 0990945f64b1
Create Date: 2026-02-17 04:35:15.553000

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "f2c4a4c8936a"
down_revision: Union[str, None] = "0990945f64b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index("ix_verses_book_id", "verses", ["book_id"], unique=False)
    op.create_index("ix_verses_translation_id", "verses", ["translation_id"], unique=False)
    op.create_index(
        "ix_verses_translation_id_book_id_chapter_verse_number",
        "verses",
        ["translation_id", "book_id", "chapter", "verse_number"],
        unique=False,
    )
    op.create_index(
        "ix_translations_canon_id", "translations", ["canon_id"], unique=False
    )


def downgrade() -> None:
    op.drop_index("ix_translations_canon_id", table_name="translations")
    op.drop_index(
        "ix_verses_translation_id_book_id_chapter_verse_number", table_name="verses"
    )
    op.drop_index("ix_verses_translation_id", table_name="verses")
    op.drop_index("ix_verses_book_id", table_name="verses")

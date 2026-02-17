"""add indexes for verses and translations

Revision ID: c3a6b5d4e2f1
Revises: 0990945f64b1
Create Date: 2026-02-17 00:00:00.000000

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c3a6b5d4e2f1"
down_revision: Union[str, None] = "0990945f64b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index("ix_verses_bookId", "verses", ["bookId"], unique=False)
    op.create_index(
        "ix_verses_translationId", "verses", ["translationId"], unique=False
    )
    op.create_index(
        "ix_verses_translationId_bookId_chapter_verseNumber",
        "verses",
        ["translationId", "bookId", "chapter", "verseNumber"],
        unique=False,
    )
    op.create_index("ix_translations_canonId", "translations", ["canonId"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_translations_canonId", table_name="translations")
    op.drop_index(
        "ix_verses_translationId_bookId_chapter_verseNumber", table_name="verses"
    )
    op.drop_index("ix_verses_translationId", table_name="verses")
    op.drop_index("ix_verses_bookId", table_name="verses")

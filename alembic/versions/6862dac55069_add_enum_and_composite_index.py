"""add enum and composite index

Revision ID: 6862dac55069
Revises: 2a22674dc1fc
Create Date: 2026-02-19

"""

from alembic import op
import sqlalchemy as sa
import enum

# ✅ These lines are REQUIRED
revision = "6862dac55069"
down_revision = "2a22674dc1fc"
branch_labels = None
depends_on = None


class PublicationType(str, enum.Enum):
    journal = "journal"
    conference = "conference"
    book_chapter = "book_chapter"
    edited_volume = "edited_volume"


def upgrade():
    publication_enum = sa.Enum(
        "journal",
        "conference",
        "book_chapter",
        "edited_volume",
        name="publicationtype"
    )

    publication_enum.create(op.get_bind(), checkfirst=True)

    op.alter_column(
        "publications",
        "publication_type",
        type_=publication_enum,
        existing_type=sa.String(),
        postgresql_using="publication_type::publicationtype"
    )

    op.create_index(
        "ix_faculty_year",
        "publications",
        ["faculty_id", "year"]
    )


def downgrade():
    op.drop_index("ix_faculty_year", table_name="publications")

    op.alter_column(
        "publications",
        "publication_type",
        type_=sa.String(),
        existing_type=sa.Enum(name="publicationtype")
    )

    sa.Enum(name="publicationtype").drop(op.get_bind(), checkfirst=True)

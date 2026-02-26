"""clean publication enum

Revision ID: e0617ea9a1f8
Revises: 067a8b3c7785
Create Date: 2026-02-21 02:35:14.418316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e0617ea9a1f8'
down_revision: Union[str, Sequence[str], None] = '067a8b3c7785'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Step 1: Create new enum
    op.execute("CREATE TYPE publication_type_enum AS ENUM ('journal', 'conference')")

    # Step 2: Alter column to TEXT temporarily
    op.execute("ALTER TABLE publications ALTER COLUMN publication_type TYPE TEXT")

    # Step 3: Convert existing values safely (optional but safe)
    op.execute("""
        UPDATE publications
        SET publication_type = 'journal'
        WHERE publication_type NOT IN ('journal', 'conference')
    """)

    # Step 4: Convert column back to ENUM
    op.execute("""
        ALTER TABLE publications
        ALTER COLUMN publication_type
        TYPE publication_type_enum
        USING publication_type::publication_type_enum
    """)
    # ### end Alembic commands ###


def downgrade():
    op.execute("ALTER TABLE publications ALTER COLUMN publication_type TYPE TEXT")
    op.execute("DROP TYPE publication_type_enum")
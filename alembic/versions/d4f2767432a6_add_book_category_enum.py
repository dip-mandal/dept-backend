from alembic import op
import sqlalchemy as sa


# revision identifiers
revision = 'd4f2767432a6'
down_revision = '107f3a46213d'
branch_labels = None
depends_on = None


def upgrade():
    book_category_enum = sa.Enum(
        'authored',
        'edited',
        'monograph',
        name='bookcategory'
    )

    book_category_enum.create(op.get_bind(), checkfirst=True)

    op.add_column(
        'books',
        sa.Column(
            'category',
            book_category_enum,
            nullable=False
        )
    )


def downgrade():
    op.drop_column('books', 'category')

    sa.Enum(
        'authored',
        'edited',
        'monograph',
        name='bookcategory'
    ).drop(op.get_bind(), checkfirst=True)

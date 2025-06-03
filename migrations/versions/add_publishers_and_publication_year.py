"""Add publishers table and publication_year, publisher_id columns to books

Revision ID: add_publishers_and_publication_year
Revises: 559f0f10e473
Create Date: 2024-06-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_publishers_and_publication_year'
down_revision = '559f0f10e473'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'publishers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), unique=True, nullable=False)
    )
    op.add_column('books', sa.Column('publication_year', sa.Integer(), nullable=True))
    op.add_column('books', sa.Column('publisher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_books_publisher_id', 'books', 'publishers', ['publisher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_books_publisher_id', 'books', type_='foreignkey')
    op.drop_column('books', 'publisher_id')
    op.drop_column('books', 'publication_year')
    op.drop_table('publishers')

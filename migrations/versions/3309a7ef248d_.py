"""empty message

Revision ID: 3309a7ef248d
Revises: abf6c1d6ebb2
Create Date: 2022-03-21 00:10:52.143923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3309a7ef248d'
down_revision = 'abf6c1d6ebb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bounty', sa.Column('image_src', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bounty', 'image_src')
    # ### end Alembic commands ###
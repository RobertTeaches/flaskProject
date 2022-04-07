"""empty message

Revision ID: a8ff573955e8
Revises: 
Create Date: 2022-03-24 15:31:36.494612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8ff573955e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'bounty_submission', 'user', ['user_id'], ['id'])
    op.add_column('user', sa.Column('plain_password', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'plain_password')
    op.drop_constraint(None, 'bounty_submission', type_='foreignkey')
    # ### end Alembic commands ###
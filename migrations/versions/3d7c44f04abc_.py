"""empty message

Revision ID: 3d7c44f04abc
Revises: 8fc1256b0b0c
Create Date: 2022-03-24 15:36:31.011131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d7c44f04abc'
down_revision = '8fc1256b0b0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bounty',
    sa.Column('id', sa.String(length=256), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('reward', sa.Integer(), nullable=True),
    sa.Column('xp', sa.Integer(), nullable=True),
    sa.Column('image_src', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('bounty', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_bounty_description'), ['description'], unique=True)
        batch_op.create_index(batch_op.f('ix_bounty_title'), ['title'], unique=True)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('nickname', sa.String(length=128), nullable=True),
    sa.Column('avatar_image', sa.String(), nullable=True),
    sa.Column('plain_password', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_first_name'), ['first_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_last_name'), ['last_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_nickname'), ['nickname'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('bounty_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=2048), nullable=True),
    sa.Column('submission_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('bounty_submission', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_bounty_submission_submission_time'), ['submission_time'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bounty_submission', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_bounty_submission_submission_time'))

    op.drop_table('bounty_submission')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_nickname'))
        batch_op.drop_index(batch_op.f('ix_user_last_name'))
        batch_op.drop_index(batch_op.f('ix_user_first_name'))

    op.drop_table('user')
    with op.batch_alter_table('bounty', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_bounty_title'))
        batch_op.drop_index(batch_op.f('ix_bounty_description'))

    op.drop_table('bounty')
    # ### end Alembic commands ###

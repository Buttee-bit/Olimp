"""add olimpiad modyle answers

Revision ID: be4113431f2a
Revises: d90b611f6b0f
Create Date: 2023-04-26 14:07:21.362153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be4113431f2a'
down_revision = 'd90b611f6b0f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_task', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('module',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('olimpiad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('time_start', sa.TIMESTAMP(), nullable=True),
    sa.Column('time_end', sa.TIMESTAMP(), nullable=True),
    sa.Column('work_time', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('task', sa.Column('id_olimpiad', sa.Integer(), nullable=True))
    op.add_column('task', sa.Column('title', sa.String(), nullable=True))
    op.add_column('task', sa.Column('module', sa.Integer(), nullable=True))
    op.add_column('task', sa.Column('type', sa.Integer(), nullable=True))
    op.add_column('task', sa.Column('description_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'description_id')
    op.drop_column('task', 'type')
    op.drop_column('task', 'module')
    op.drop_column('task', 'title')
    op.drop_column('task', 'id_olimpiad')
    op.drop_table('olimpiad')
    op.drop_table('module')
    op.drop_table('answer')
    # ### end Alembic commands ###

"""add user answer + total score

Revision ID: 9cba0f2a3fc3
Revises: 1255be3a8823
Create Date: 2023-04-26 17:13:12.313988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cba0f2a3fc3'
down_revision = '1255be3a8823'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('olimpiad', sa.Column('order', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('olimpiad', 'order')
    # ### end Alembic commands ###

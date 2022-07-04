"""add phone number

Revision ID: 226e07cd5dfc
Revises: 55db0b355edb
Create Date: 2022-07-03 18:29:24.863795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '226e07cd5dfc'
down_revision = '55db0b355edb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###

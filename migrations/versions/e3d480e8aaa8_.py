"""empty message

Revision ID: e3d480e8aaa8
Revises: ab08e9ce87ce
Create Date: 2023-08-26 20:46:35.274267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3d480e8aaa8'
down_revision = 'ab08e9ce87ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uuid', sa.UUID(), nullable=False))
        batch_op.drop_column('uid')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uid', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.drop_column('uuid')

    # ### end Alembic commands ###

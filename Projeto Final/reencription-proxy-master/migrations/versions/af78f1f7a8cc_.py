"""empty message

Revision ID: af78f1f7a8cc
Revises: c6f48f3a4dfb
Create Date: 2023-04-14 00:30:10.088373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af78f1f7a8cc'
down_revision = 'c6f48f3a4dfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_key_signer_patient', sa.String(length=256), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('token', schema=None) as batch_op:
        batch_op.drop_column('public_key_signer_patient')

    # ### end Alembic commands ###
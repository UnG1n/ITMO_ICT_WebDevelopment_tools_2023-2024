"""migration_1

Revision ID: 3d063aedcedf
Revises: 
Create Date: 2024-08-25 19:31:09.003895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3d063aedcedf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('budget', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'budget', 'user', ['user_id'], ['id'])
    op.add_column('category', sa.Column('user_id', sa.Integer(), nullable=False))
    op.add_column('category', sa.Column('budget_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'category', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'category', 'budget', ['budget_id'], ['id'])
    op.add_column('goal', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'goal', 'user', ['user_id'], ['id'])
    op.add_column('notification', sa.Column('transaction_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'notification', 'transaction', ['transaction_id'], ['id'])
    op.add_column('transaction', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'transaction', 'user', ['user_id'], ['id'])
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint(None, 'transaction', type_='foreignkey')
    op.drop_column('transaction', 'user_id')
    op.drop_constraint(None, 'notification', type_='foreignkey')
    op.drop_column('notification', 'transaction_id')
    op.drop_constraint(None, 'goal', type_='foreignkey')
    op.drop_column('goal', 'user_id')
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_column('category', 'budget_id')
    op.drop_column('category', 'user_id')
    op.drop_constraint(None, 'budget', type_='foreignkey')
    op.drop_column('budget', 'user_id')
    # ### end Alembic commands ###

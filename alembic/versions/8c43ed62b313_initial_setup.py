"""Initial setup

Revision ID: 8c43ed62b313
Revises: 
Create Date: 2025-04-16 14:24:50.891372

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c43ed62b313'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('address', sa.Date(), nullable=True),
    sa.Column('cnss_number', sa.String(), nullable=True),
    sa.Column('contract_type', sa.Enum('Cdi', 'Cdd', 'Sivp', 'Apprenti', name='contracttype'), nullable=True),
    sa.Column('gender', sa.Enum('Male', 'Female', name='gender'), nullable=False),
    sa.Column('Account_status', sa.Enum('Active', 'Inactive', name='accountstatus'), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.CheckConstraint("(contract_type IN ('Cdi', 'Cdd') AND cnss_number IS NOT NULL AND cnss_number ~ '^\\d{8}-\\d{2}$') OR (contract_type IN ('Apprenti', 'Sivp') AND (cnss_number IS NULL OR cnss_number ~ '^\\d{8}-\\d{2}$'))", name='ck_employees_cnss_number'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('employee_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.Enum('Admin', 'InventoryManager', 'SuperUser', 'Vendor', name='roletype'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jwt_blacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('account_activation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('Used', 'Pending', name='tokenstatus'), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reset_password',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('Used', 'Pending', name='tokenstatus'), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reset_password')
    op.drop_table('account_activation')
    op.drop_table('jwt_blacklist')
    op.drop_table('employee_roles')
    op.drop_table('employee')
    # ### end Alembic commands ###

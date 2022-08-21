"""Initial Migration

Revision ID: 423570364338
Revises: 
Create Date: 2022-08-02 13:07:23.151279

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '423570364338'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('layer_type',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('layer',
    sa.Column('icons', sa.JSON(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('layer_type_id', sa.Integer(), nullable=True),
    sa.Column('search_fields', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('view_fields', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['layer_type_id'], ['layer_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dashboard',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('superset_dashboard_id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('layer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['layer_id'], ['layer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dashboard_filter',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('dashboard_id', sa.Integer(), nullable=True),
    sa.Column('filter_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('field_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('value', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['dashboard_id'], ['dashboard.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('dashboard_filter')
    op.drop_table('dashboard')
    op.drop_table('layer')
    op.drop_table('layer_type')

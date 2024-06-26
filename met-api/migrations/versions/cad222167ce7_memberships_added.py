"""memberships added

Revision ID: cad222167ce7
Revises: 5880bead8f03
Create Date: 2023-01-24 14:31:48.024605

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cad222167ce7'
down_revision = '5880bead8f03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    membership_status_codes = op.create_table('membership_status_codes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status_name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('membership',
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('engagement_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Enum('TEAM_MEMBER', name='membershiptype'), nullable=False),
    sa.Column('created_by', sa.String(length=50), nullable=True),
    sa.Column('updated_by', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['engagement_id'], ['engagement.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['status'], ['membership_status_codes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['met_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(membership_status_codes, [
        {'id': 1, 'status_name': 'ACTIVE', 'description': 'Active Membership', 'created_date': datetime.utcnow(),
         'updated_date': datetime.utcnow()},
        {'id': 2, 'status_name': 'INACTIVE', 'description': 'Inactive Membership', 'created_date': datetime.utcnow(),
         'updated_date': datetime.utcnow()}
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('membership')
    op.drop_table('membership_status_codes')
    op.execute("""DROP TYPE membershiptype""")
    # ### end Alembic commands ###
